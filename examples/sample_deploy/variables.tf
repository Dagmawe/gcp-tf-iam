variable "project_name" {
  type        = string
  description = "The name of the project."
  default     = "test-project1"
}

variable "project_id" {
  type        = string
  description = "The ID of the project."
  default     = "test-project1"
}

variable "folder_id" {
  type        = string
  description = "The folder ID where the project will be created."
}

variable "billing_account" {
  type        = string
  description = "The billing account ID to associate with the project."
}

variable "network_name" {
  type        = string
  description = "The name of the VPC network."
  default     = "test-network"
}

variable "subnet_name" {
  type        = string
  description = "The name of the subnet."
  default     = "test-subnet"
}

variable "subnet_ip" {
  type        = string
  description = "The IP CIDR range for the subnet."
  default     = "10.10.0.0/24"
}

variable "subnet_region" {
  type        = string
  description = "The region where the subnet will be created."
  default     = "us-central1"
}
