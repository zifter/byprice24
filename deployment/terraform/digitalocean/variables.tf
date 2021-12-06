variable "name" {
  description = "prefix for all resources name"
  type        = string
}

variable "k8s_version" {
  description = "K8S Cluster Version"
  type        = string
}

variable "postgres_version" {
  description = "Postgres Cluster Version"
  type        = string
}
