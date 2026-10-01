###################
## LAMBDAS ROLE ###
###################
resource "aws_iam_role" "lambda_role" {
  name = "project-${var.environment}-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "lambda" {

  name = "project-${var.environment}-lambda-policies"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "lambda:InvokeFunction"
        ]
        Resource = [
           for function_name in local.lambdas : "arn:aws:lambda:${local.region}:${local.account_id}:function:${function_name}"
        ]
      },
      {
        Effect = "Allow",
        Action = [
          "s3:GetObject",
          "s3:GetBucketAcl",
          "s3:ListBucket",
          "s3:ListObjects",
          "s3:ListObjectsV2",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:DeleteObject"
        ],
        Resource = flatten([
          for bucket_name in local.buckets : [
            "arn:aws:s3:::${bucket_name}-${local.region}-${local.account_id}-${var.environment}",
            "arn:aws:s3:::${bucket_name}-${local.region}-${local.account_id}-${var.environment}/*"
          ]
        ])
      },
      {
        Effect = "Allow",
        Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_execution_role_policy_attachment" {
  policy_arn = aws_iam_policy.lambda.arn
  role       = aws_iam_role.lambda_role.name
}