##########################################
## ASSING PERIODICITY TO STATE MACHINE ###
##########################################
resource "aws_cloudwatch_event_rule" "create_eventbridge_rules" {
  for_each = { for config in local.event_rule_configs : config.name => config }
  name  = each.value.name
  description = each.value.config.description
  schedule_expression = each.value.config.schedule_expression
  role_arn = "arn:aws:iam::${local.account_id}:role/${var.eventbridge_role}"
}

resource "aws_cloudwatch_event_target" "states_machines_target" {
  for_each = { for config in local.event_rule_configs : config.name => config }
  rule      = aws_cloudwatch_event_rule.create_eventbridge_rules[each.key].name
  arn       = aws_sfn_state_machine.create_states_machines[each.value.config.state_machine].arn
  input     = jsonencode({ 
    "PARAMETERS" : each.value.config.PARAMETERS,
    "BUCKET_DATA": "${var.data_buckets_name}-${local.region}-${local.account_id}-${var.environment}",
    "BUCKET_ARTIFACT": "${var.artifacts_buckets_name}-${local.region}-${local.account_id}-${var.environment}",
    "BUCKET_MODEL": "${var.ml_buckets_name}-${local.region}-${local.account_id}-${var.environment}",
    "DEVMODE": "True"
    })
  role_arn = "arn:aws:iam::${local.account_id}:role/${var.eventbridge_role}"
}