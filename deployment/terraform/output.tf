output "k8s_cluster_id" {
  description = "Cluster ID"
  value       = module.infra.k8s_cluster_id
}

output "k8s_kube_config" {
  description = "Cluster ID"
  value       = module.infra.k8s_kube_config
}

output "postgres_host" {
  description = "Postgres host"
  value       = module.infra.postgres_host
}

output "postgres_user" {
  description = "Postgres user"
  value       = module.infra.postgres_user
}

output "postgres_pass" {
  description = "Postgres password"
  value       = module.infra.postgres_pass
}

output "postgres_port" {
  description = "Postgres port"
  value       = module.infra.postgres_port
}
