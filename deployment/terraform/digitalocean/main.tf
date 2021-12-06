locals {
  postgres_instance = "db-s-1vcpu-1gb"
  k9s_node_instance = "s-2vcpu-4gb"
  region = "fra1"
}

resource "digitalocean_project" "project" {
  name        = var.name
  description = "A project to represent development resources."
  purpose     = "Web Application"
  environment = "Staging"
}

resource "digitalocean_vpc" "vpc" {
  name     = "vpc-${var.name}"
  region   = local.region
  ip_range = "10.10.10.0/24"
}

resource "digitalocean_database_cluster" "postgres" {
  name       = "postgres-${var.name}"
  engine     = "pg"
  version    = var.postgres_version
  size       = local.postgres_instance
  region     = local.region
  node_count = 1
  private_network_uuid = digitalocean_vpc.vpc.id
}

resource "digitalocean_kubernetes_cluster" "cluster" {
  name   = "k8s-${var.name}"
  region = local.region

  # doctl kubernetes options versions
  version = var.k8s_version
  vpc_uuid = digitalocean_vpc.vpc.id

  node_pool {
    name       = "worker-pool-autoscale"
    size       = local.k9s_node_instance
    auto_scale = true
    min_nodes  = 1
    max_nodes  = 2
  }
}

data "digitalocean_project" "staging" {
  name = var.name
}

resource "digitalocean_project_resources" "project_resources" {
  project = data.digitalocean_project.staging.id
  resources = [
    digitalocean_database_cluster.postgres.urn,
    digitalocean_kubernetes_cluster.cluster.urn,
  ]
}
