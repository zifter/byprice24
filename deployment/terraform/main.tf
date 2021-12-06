locals {
  project_name     = "byprice24"

  k8s_version      = "1.21.5-do.0"
  cluster_name     = "k8s-byprice24"
  postgres_name    = "db-postgresql-fra1-85185"
  region           = "fra1"
  postgres_version = "11"
}

module "infra" {
  source = "./digitalocean"

  name              = local.project_name
  k8s_version       = local.k8s_version
  postgres_version  = local.postgres_version
}

data "github_actions_public_key" "example_public_key" {
  repository = "byprice24"
}

resource "github_actions_secret" "k8s_kube_config" {
  repository       = "byprice24"
  secret_name      = "KUBECONFIG"
  plaintext_value  = module.infra.k8s_kube_config
}

resource "github_actions_secret" "postgres_user" {
  repository       = "byprice24"
  secret_name      = "POSTGRES_USER"
  plaintext_value  = module.infra.postgres_user
}

resource "github_actions_secret" "postgres_pass" {
  repository       = "byprice24"
  secret_name      = "POSTGRES_PASS"
  plaintext_value  = module.infra.postgres_pass
}

resource "github_actions_secret" "postgres_host" {
  repository       = "byprice24"
  secret_name      = "POSTGRES_HOST"
  plaintext_value  = module.infra.postgres_host
}

resource "github_actions_secret" "postgres_port" {
  repository       = "byprice24"
  secret_name      = "POSTGRES_PORT"
  plaintext_value  = module.infra.postgres_port
}

resource "github_actions_secret" "postgres_database" {
  repository       = "byprice24"
  secret_name      = "POSTGRES_DATABASE"
  plaintext_value  = module.infra.postgres_database
}
