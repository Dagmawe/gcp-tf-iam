import unittest
from unittest.mock import patch, MagicMock
import os
import json
from tf_iam.tool import find_gcp_api_method, get_iam_permission

class TestTool(unittest.TestCase):

    def setUp(self):
        # Clear cache before tests to ensure isolation
        self.cache_dir = ".cache"
        if os.path.exists(self.cache_dir):
            import shutil
            shutil.rmtree(self.cache_dir)

    def tearDown(self):
        # Clean up cache after tests
        if os.path.exists(self.cache_dir):
            import shutil
            shutil.rmtree(self.cache_dir)

    @patch('urllib.request.urlopen')
    def test_find_gcp_api_method_hits_internet_and_caches(self, mock_urlopen):
        # Setup mock network response
        mock_response = MagicMock()
        mock_data = {
            "resources": {
                "buckets": {
                    "methods": {
                        "get": {
                            "httpMethod": "GET",
                            "path": "b/{bucket}",
                            "id": "storage.buckets.get"
                        }
                    }
                }
            }
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Run function
        method_id = find_gcp_api_method(
            discovery_url="https://www.googleapis.com/discovery/v1/apis/storage/v1/rest",
            target_http_method="GET",
            target_path="b/my-bucket"
        )

        self.assertEqual(method_id, "storage.buckets.get")
        
        # Verify cache file was created
        cache_file = os.path.join(".cache", "discovery", "storage_v1.json")
        self.assertTrue(os.path.exists(cache_file))

    @patch('urllib.request.urlopen')
    def test_get_iam_permission_hits_internet_and_caches(self, mock_urlopen):
        # Setup mock network response
        mock_response = MagicMock()
        mock_data = {
            "storage.buckets.get": {
                "permissions": [{"name": "storage.buckets.get"}]
            }
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Run function
        perms = get_iam_permission("storage.buckets.get")

        self.assertEqual(perms, ["storage.buckets.get"])
        
        # Verify cache file was created
        cache_file = os.path.join(".cache", "map.json")
        self.assertTrue(os.path.exists(cache_file))

    @patch('urllib.request.urlopen')
    def test_get_iam_permission_falls_back_to_local_json(self, mock_urlopen):
        # Setup mock network response (empty map, so search fails)
        mock_response = MagicMock()
        mock_data = {} # Empty dataset
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Run function for a method we know is in fallback_map.json
        perms = get_iam_permission("compute.instances.insert")

        # Fallback map for compute.instances.insert should contain compute.instances.create, etc.
        self.assertIn("compute.instances.create", perms)

    @patch('urllib.request.urlopen')
    def test_find_gcp_api_method_requires_full_path_match(self, mock_urlopen):
        # Resource order mirrors the real compute discovery doc: 'instances' before 'zones',
        # and 'insert' before 'setMetadata' alphabetically. A substring match would resolve
        # ".../instances/vm1/setMetadata" to instances.insert and ".../instances/vm1" to zones.get.
        mock_response = MagicMock()
        mock_data = {
            "resources": {
                "instances": {
                    "methods": {
                        "get": {"httpMethod": "GET", "path": "projects/{project}/zones/{zone}/instances/{instance}", "id": "compute.instances.get"},
                        "insert": {"httpMethod": "POST", "path": "projects/{project}/zones/{zone}/instances", "id": "compute.instances.insert"},
                        "setMetadata": {"httpMethod": "POST", "path": "projects/{project}/zones/{zone}/instances/{instance}/setMetadata", "id": "compute.instances.setMetadata"},
                    }
                },
                "zones": {
                    "methods": {
                        "get": {"httpMethod": "GET", "path": "projects/{project}/zones/{zone}", "id": "compute.zones.get"},
                    }
                },
            }
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response
        discovery_url = "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest"

        cases = {
            ("POST", "v1/projects/p/zones/us-central1-a/instances"): "compute.instances.insert",
            ("POST", "v1/projects/p/zones/us-central1-a/instances/vm1/setMetadata"): "compute.instances.setMetadata",
            ("GET", "v1/projects/p/zones/us-central1-a/instances/vm1"): "compute.instances.get",
            ("GET", "v1/projects/p/zones/us-central1-a"): "compute.zones.get",
            ("POST", "v1/projects/p/zones/us-central1-a/instances/vm1/stop"): None,  # not in doc -> no false positive
        }
        for (verb, path), expected in cases.items():
            with self.subTest(verb=verb, path=path):
                self.assertEqual(find_gcp_api_method(discovery_url, verb, path, quiet=True), expected)

    @patch('urllib.request.urlopen')
    def test_find_gcp_api_method_reserved_expansion_spans_segments(self, mock_urlopen):
        # {+name} style templates (e.g. Pub/Sub) must still match multi-segment resource names.
        mock_response = MagicMock()
        mock_data = {
            "resources": {
                "projects": {
                    "resources": {
                        "topics": {
                            "methods": {
                                "create": {"httpMethod": "PUT", "path": "v1/{+name}", "id": "pubsub.projects.topics.create"},
                            }
                        }
                    }
                }
            }
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response
        discovery_url = "https://www.googleapis.com/discovery/v1/apis/pubsub/v1/rest"

        self.assertEqual(
            find_gcp_api_method(discovery_url, "PUT", "pubsub/projects/p/topics/my-topic", quiet=True),
            "pubsub.projects.topics.create",
        )

    @patch('tf_iam.tool.get_iam_permission', return_value=["compute.instances.create"])
    @patch('tf_iam.tool.find_gcp_api_method', return_value="compute.instances.insert")
    def test_process_log_parses_bodies_and_repeated_methods(self, _mock_find, _mock_perms):
        # Two POSTs of the same method; only the second one uses a CMEK key. The body must be
        # parsed from the modern log format (bare logger prefix as blank line, dashes terminator)
        # and the conditional permission of the *second* call must still be reported.
        p = "2026-01-01T00:00:00.000Z [DEBUG] provider.terraform-provider-google_v8.10.0_x5"
        def request_block(body_lines):
            lines = [
                f"{p}: ---[ REQUEST ]---------------------------------------",
                f"{p}: POST /compute/v1/projects/p/zones/us-central1-a/instances?alt=json HTTP/1.1",
                f"{p}: Host: 127.0.0.1:8080",
                f"{p}: Content-Type: application/json",
                f"{p}",  # empty line between headers and body is logged as a bare prefix
            ]
            lines += [f"{p}: {l}" for l in body_lines]
            lines += [
                f"{p}: -----------------------------------------------------",
                f"{p}: 2026/01/01 00:00:00 [DEBUG] Google API Response Details:",
                f"{p}: ---[ RESPONSE ]--------------------------------------",
                f"{p}: HTTP/1.0 200 OK",
                f"{p}",
                f"{p}: {{}}",
                f"{p}: -----------------------------------------------------",
            ]
            return lines
        log_lines = request_block(['{', ' "name": "vm1"', '}'])
        log_lines += request_block(['{', ' "name": "vm2",', ' "disks": [{"diskEncryptionKey": {"kmsKeyName": "projects/p/locations/l/keyRings/k/cryptoKeys/c"}}]', '}'])
        log_path = os.path.join(self.cache_dir, "synthetic.log")
        os.makedirs(self.cache_dir, exist_ok=True)
        with open(log_path, "w") as f:
            f.write("\n".join(log_lines) + "\n")

        import io, contextlib
        from tf_iam.tool import process_terraform_log
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            process_terraform_log(log_path)
        output = out.getvalue()

        self.assertIn("Payload keys: ['name']", output)
        self.assertIn("Payload keys: ['name', 'disks']", output)
        self.assertIn("- cloudkms.cryptoKeyVersions.useToEncrypt", output)
        self.assertIn("- compute.instances.create", output)

if __name__ == "__main__":
    unittest.main()
