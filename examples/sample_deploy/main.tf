resource "google_project" "project" {
  name                = var.project_name
  project_id          = var.project_id
  folder_id           = var.folder_id
  billing_account     = var.billing_account
  auto_create_network = false
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
