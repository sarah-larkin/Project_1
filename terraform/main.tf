#backend bucket created before the initial terraform init --> aws s3 mb s3://sl-terraform-backend-bucket

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.3.0"
    }
  
    }
    backend "s3" {
        bucket = "sl-terraform-backend-bucket"    #this bucket can be used for other projects
        key    = "project-1/terraform.tfstate"    #this key should be used to identify which project it is for 
        region = "eu-west-2"
    }
}


provider "aws" {
  region = "eu-west-2"
}

#make sure future projects have an updated key if using the same backend bucket!!