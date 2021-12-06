terraform {
  backend "remote" {
    organization = "byprice24"
    workspaces {
      name = "byprice24"
    }
  }

  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
  required_version = ">= 0.13"
}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.do_token
}

provider "github" {
  token = var.github_token # or `GITHUB_TOKEN`
}
