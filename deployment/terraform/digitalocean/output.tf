output "k8s_cluster_id" {
  description = "Cluster ID"
  value       = digitalocean_kubernetes_cluster.cluster.id
}

output "k8s_kube_config" {
  description = "Cluster Kube Config"
  value       = digitalocean_kubernetes_cluster.cluster.kube_config[0].raw_config
}

output "postgres_host" {
  description = "Postgres host"
  value       = digitalocean_database_cluster.postgres.private_host
}

output "postgres_user" {
  description = "Postgres username"
  value       = digitalocean_database_cluster.postgres.user
}

output "postgres_pass" {
  description = "Postgres password"
  value       = digitalocean_database_cluster.postgres.password
}

output "postgres_port" {
  description = "Postgres database port"
  value       = digitalocean_database_cluster.postgres.port
}

output "postgres_database" {
  description = "Postgres default database"
  value       = digitalocean_database_cluster.postgres.database
}
