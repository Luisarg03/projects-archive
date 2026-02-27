##################
## EVENTS ROLE ###
##################
resource "aws_iam_role" "eventbridge" {
  name = "project-${var.environment}-eventbridge-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "events.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "eventbridge" {
  name = "project-${var.environment}-eventbridge-policies"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "events:PutRule",
          "events:PutTargets"
        ]
        Resource = [
          for event_name in local.events_rules : "arn:aws:events:${local.region}:${local.account_id}:rule/${event_name}"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "states:StartExecution"
        ]
        Resource = [
          for sm_name in local.states_machines : "arn:aws:states:${local.region}:${local.account_id}:stateMachine:${sm_name}"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "eventbridge" {
  policy_arn = aws_iam_policy.eventbridge.arn
  role = aws_iam_role.eventbridge.name
}