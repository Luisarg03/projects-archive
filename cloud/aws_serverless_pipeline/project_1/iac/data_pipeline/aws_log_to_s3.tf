locals {
  logs_groups = [
    "/aws/lambda/project_raw_daily",
    "/aws/lambda/project_cur_daily",
    "/aws-glue/jobs/error"
  ]
}

data "aws_lambda_function" "existing" {
  function_name = "project_logswriter"
}

data "aws_iam_role" "existing" {
  name = "${var.lambda_role}"
}

resource "aws_lambda_permission" "allow_cloudwatch_logs" {
  statement_id  = "AllowExecutionFromCloudWatchLogs"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.existing.function_name
  principal     = "logs.amazonaws.com"
}

resource "aws_cloudwatch_log_subscription_filter" "loggroupfilter" {
  for_each = toset(local.logs_groups)
  name = replace(each.value, "/", "_")
  log_group_name = each.value
  filter_pattern = ""
  destination_arn = data.aws_lambda_function.existing.arn
}
