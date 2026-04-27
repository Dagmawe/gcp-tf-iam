import unittest
from tf_iam.rules_engine import evaluate_conditional_permissions

class TestRulesEngine(unittest.TestCase):

    def test_compute_network_use(self):
        body = {
            "networkInterfaces": [
                {"network": "projects/host-np-project1/global/networks/test"}
            ]
        }
        perms = evaluate_conditional_permissions("compute.instances.insert", body)
        self.assertIn("compute.networks.use", perms)

    def test_compute_subnetwork_use(self):
        body = {
            "networkInterfaces": [
                {"subnetwork": "projects/host-np-project1/regions/us-central1/subnetworks/test"}
            ]
        }
        perms = evaluate_conditional_permissions("compute.instances.insert", body)
        self.assertIn("compute.subnetworks.use", perms)

    def test_compute_image_use(self):
        body = {
            "disks": [
                {"initializeParams": {"sourceImage": "debian-cloud/debian-12"}}
            ]
        }
        perms = evaluate_conditional_permissions("compute.instances.insert", body)
        self.assertIn("compute.images.useReadOnly", perms)

    def test_storage_cmek_use(self):
        body = {
            "encryption": {
                "defaultKmsKeyName": "projects/test/locations/us/keyRings/kr/cryptoKeys/key"
            }
        }
        perms = evaluate_conditional_permissions("storage.buckets.insert", body)
        self.assertIn("cloudkms.cryptoKeyVersions.useToEncrypt", perms)

    def test_generic_kms_rule(self):
        body = {
            "someRandomField": {
                "kmsKeyName": "projects/test/locations/us/keyRings/kr/cryptoKeys/key"
            }
        }
        perms = evaluate_conditional_permissions("some.unknown.method", body)
        self.assertIn("cloudkms.cryptoKeyVersions.useToEncrypt", perms)

if __name__ == "__main__":
    unittest.main()
