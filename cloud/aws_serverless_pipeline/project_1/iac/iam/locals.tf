data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

###################
### LOCALS VARS ###
###################
locals {
  account_id = data.aws_caller_identity.current.account_id
  region = data.aws_region.current.name
  lambdas = toset(var.lambdas_names)
  buckets = toset(var.buckets_names)
  states_machines = toset(var.states_machines_names)
  events_rules = toset(var.events_rules_names)
  glue_jobs = toset(var.glue_jobs_names)
}