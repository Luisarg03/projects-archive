#############################
### CREATE STATES MACHINE ###
#############################
resource "aws_sfn_state_machine" "create_states_machines" {
  for_each = { for config in local.state_machine_configs : config.name => config }
  name = each.value.name
  role_arn = "arn:aws:iam::${local.account_id}:role/${var.stepfunctions_role}"
  depends_on = [
    aws_lambda_function.create_wellington_lambdas_functions,
    aws_lambda_function.create_sap_lambdas_functions
  ]
  definition = jsonencode(each.value.config)

  tags = {
    Terraform   = "true"
    Environment = "${var.environment}"
  }
}