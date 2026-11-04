resource "google_project" "project" {
  name                = var.project_name
  project_id          = var.project_id
  folder_id           = var.folder_id
  billing_account     = var.billing_account
  auto_create_network = false
  # Provider default is "PREVENT", which blocks `terraform destroy` (and therefore a destroy dry-run).
  deletion_policy = "DELETE"
}

resource "google_compute_network" "network" {
  name                            = var.network_name
  auto_create_subnetworks         = false
  routing_mode                    = "GLOBAL"
  project                         = google_project.project.project_id
  delete_default_routes_on_create = false
}

resource "google_compute_subnetwork" "subnetwork" {
  name                     = var.subnet_name
  ip_cidr_range            = var.subnet_ip
  region                   = var.subnet_region
  network                  = google_compute_network.network.name
  project                  = google_project.project.project_id
  private_ip_google_access = false
}

output "project_id" {
  description = "The ID of the created project."
  value       = google_project.project.project_id
}

output "network_id" {
  description = "The ID of the created VPC network."
  value       = google_compute_network.network.id
}

output "subnet_id" {
  description = "The ID of the created subnet."
  value       = google_compute_subnetwork.subnetwork.id
}

resource "google_pubsub_topic" "test-topic" {
  name    = "test-topic"
  project = google_project.project.project_id
}

resource "google_storage_bucket" "test-bucket" {
  name                        = "test-bucket-tf-iam-dryrun-example"
  location                    = "US"
  project                     = google_project.project.project_id
  uniform_bucket_level_access = true
}

resource "google_compute_instance" "vm" {
  name         = "test-instance"
  project      = google_project.project.project_id
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
    kms_key_self_link = "projects/test-project1/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key"
  }

  network_interface {
    network    = google_compute_network.network.id
    subnetwork = google_compute_subnetwork.subnetwork.id
  }
}

resource "google_service_account" "sa" {
  account_id   = "test-sa"
  display_name = "Test Service Account"
  project      = google_project.project.project_id
}

resource "google_project_iam_member" "sa-member" {
  project = google_project.project.project_id
  role    = "roles/viewer"
  member  = "serviceAccount:${google_service_account.sa.email}"
}

resource "google_dns_managed_zone" "dns-zone" {
  name        = "test-zone"
  dns_name    = "testzone.example.com."
  description = "Test DNS Zone"
  project     = google_project.project.project_id
}

resource "google_sql_database_instance" "db" {
  name             = "test-db-instance"
  region           = "us-central1"
  database_version = "POSTGRES_14"
  project          = google_project.project.project_id
  # Provider default is true, which blocks `terraform destroy` (and therefore a destroy dry-run).
  deletion_protection = false
  settings {
    tier = "db-f1-micro"
  }
}


