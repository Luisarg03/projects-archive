#########################
### GLUE JOB CREATION ###
#########################
data "aws_iam_role" "glue" {
  name = "project-dev-glue-role"
}

resource "aws_glue_job" "glue_jobs" {
  for_each = var.glue_jobs_vars
  name     = each.value["name"]
  role_arn = data.aws_iam_role.glue.arn
  
  worker_type = each.value["worker_type"]
  number_of_workers = each.value["number_workers"]
  max_retries = each.value["max_retries"]
  timeout = each.value["timeout"]
  glue_version = each.value["glue_version"]
  execution_property {
      max_concurrent_runs = each.value["max_concurrent_runs"]
  }

  command {
    script_location = "s3://${var.artifacts_buckets_name}-${local.region}-${local.account_id}-${var.environment}/${each.value["script_location"]}.py"
    name = each.value["command_name"]
    python_version  = each.value["command_python_version"]
  }

  default_arguments = each.value["args"]
}