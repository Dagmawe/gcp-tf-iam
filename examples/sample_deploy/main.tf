# Create a new GCP Project
resource "google_project" "my_new_project" {
  name       = "gcptestproject"
  project_id = var.project_id

  billing_account = "014CD6-C5F571-D1FFA4"
  folder_id       = "663111463644"

}

# Enable the Compute Engine API
resource "google_project_service" "compute_api" {
  project = var.project_id
  service = "compute.googleapis.com"

  disable_on_destroy = false
  depends_on         = [google_project.my_new_project]
}

resource "google_compute_network" "test_vpc" {
  name                    = "my-test-vpc-2026"
  project                 = var.project_id
  auto_create_subnetworks = false

  # 👈 Wait for the API to be fully enabled before creating networking
  depends_on = [google_project_service.compute_api]
}

resource "google_compute_subnetwork" "test_subnet" {
  name          = "my-test-subnet-2026"
  project       = var.project_id
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.test_vpc.id
  depends_on    = [google_project_service.compute_api]
}

resource "google_storage_bucket" "my_bucket" {
  project  = var.project_id
  name     = "my-unique-simple-gcp-bucket-2026-demo1" # 👈 Made globally unique!
  location = "US"

  storage_class = "STANDARD"

  uniform_bucket_level_access = true

  # Allows Terraform to delete the bucket even if it contains objects (useful for testing)
  force_destroy = true

  # Good security practice: prevents making the bucket public
  public_access_prevention = "enforced"
}


# Create a simple Compute Engine VM
resource "google_compute_instance" "test_vm" {
  project      = var.project_id
  name         = "my-test-vm-2026"
  machine_type = "f1-micro" # The smallest and cheapest VM type
  zone         = "us-central1-a"
  depends_on   = [google_project_service.compute_api]


  # Define the Operating System image
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  # Connect it to the newly created VPC network
  network_interface {
    network    = google_compute_network.test_vpc.id
    subnetwork = google_compute_subnetwork.test_subnet.id
  }

  # Enable Shielded VM features to satisfy Org Policy constraint
  shielded_instance_config {
    enable_secure_boot = true
  }
}



