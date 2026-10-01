terraform {
  backend "s3" {
    bucket = "project-artifacts-{region}-{id}-dev"
    key    = "state_pipeline_data/terraform.tfstate"
    region = "us-east-1"
  }
}