# TODO:
##########################################
## GENERATION OF ZIP FILES FOR LAMBDAS ###
##########################################
data "archive_file" "create_lambdas_zip" {
  for_each = local.lambdas_names
  type = "zip"
  source_dir = "${local.path_base}/lambdas/${each.value}/"
  output_path = "${local.path_base}/lambdas_zip/${each.value}.zip"
}

####################################
### UPLOAD ARTIFACTS FILES TO S3 ###
####################################
resource "aws_s3_object" "upload_artifacts" {
  for_each = fileset("${local.path_base}/", "**")
  bucket = "${var.artifacts_buckets_name}-${local.region}-${local.account_id}-${var.environment}"
  key    = "${each.value}"
  source = "${local.path_base}/${each.value}"
  etag = filemd5("${local.path_base}/${each.value}")
  depends_on = [
    data.archive_file.create_lambdas_zip
  ]
  tags = {
    Terraform  = "true" 
    Project = var.project_name
    Environment = var.environment
  }
}

####################
# CREATE LAMBDAS ###
####################
resource "aws_lambda_function" "create_globals_functions" {
  for_each = var.lambdas_global_vars
  function_name = each.value["function_name"]
  description = each.value["description"]
  role = "arn:aws:iam::${local.account_id}:role/${var.lambda_role}"
  filename = data.archive_file.create_lambdas_zip[each.value["data_code"]].output_path
  source_code_hash = data.archive_file.create_lambdas_zip[each.value["data_code"]].output_base64sha256
  handler = each.value["handler"]
  runtime = each.value["runtime"]
  timeout = each.value["timeout"]
  memory_size = each.value["memory_size"]
  architectures = [each.value["architectures"]]
  layers = []

  environment {
    variables = {
      BUCKET_LOGS = "${var.logs_buckets_name}-${local.region}-${local.account_id}-${var.environment}"
      }
  }

  # vpc_config {
  #   subnet_ids = data.aws_subnet_ids.selected.ids
  #   security_group_ids = [var.security_group_id]
  # }

  tags = {
    Terraform   = "true"
    Environment = "${var.environment}"
  }
}


resource "aws_lambda_function" "create_project_lambdas_functions" {
  for_each = var.lambdas_project_vars
  function_name = each.value["function_name"]
  description = each.value["description"]
  role = "arn:aws:iam::${local.account_id}:role/${var.lambda_role}"
  filename = data.archive_file.create_lambdas_zip[each.value["data_code"]].output_path
  source_code_hash = data.archive_file.create_lambdas_zip[each.value["data_code"]].output_base64sha256
  handler = each.value["handler"]
  runtime = each.value["runtime"]
  timeout = each.value["timeout"]
  memory_size = each.value["memory_size"]
  architectures = [each.value["architectures"]]
  layers = [
    each.value["layers_1"]
  ]

  # vpc_config {
  #   subnet_ids = data.aws_subnet_ids.selected.ids
  #   security_group_ids = [var.security_group_id]
  # }

  tags = {
    Terraform   = "true"
    Environment = "${var.environment}"
  }
}