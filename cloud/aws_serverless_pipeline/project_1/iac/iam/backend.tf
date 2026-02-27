terraform {
  backend "s3" {
    bucket = "project-artifacts-us-east-1-493161104955-dev"
    key    = "state_pipeline_iam/terraform.tfstate"
    region = "us-east-1"
  }
}