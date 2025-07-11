terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.3.0"
    }
  
    }
    backend "s3" {
        bucket = "project-1-backend"
        key    = "state/terraform.tfstate"
        region = "eu-west-2"
    }
}


provider "aws" {
  region = "eu-west-2"
}

