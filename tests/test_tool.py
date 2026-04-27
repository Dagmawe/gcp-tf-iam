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

if __name__ == "__main__":
    unittest.main()
