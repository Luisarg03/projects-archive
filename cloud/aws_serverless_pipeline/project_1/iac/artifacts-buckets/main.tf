data "aws_caller_identity" "current" {}

#########################
### CREATE S3 BUCKETS ###
#########################
locals {
  buckets = toset(var.artifacts_buckets_name)
}

resource "aws_s3_bucket" "create_s3_bucket" {
  for_each = local.buckets
  bucket = "${each.key}-${var.aws_region}-${data.aws_caller_identity.current.account_id}-${var.environment}"
  tags = {
    Terraform   = "true"
    Proyect = var.project_name
  }
}

### SonarCloud recomentacion ###
resource "aws_s3_bucket_policy" "noncompliantbucketpolicy" {
  for_each = local.buckets
  bucket = aws_s3_bucket.create_s3_bucket[each.key].id

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "mynoncompliantbucketpolicy"
    Statement = [
      {
        Sid       = "HTTPSOnly"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource = [
          aws_s3_bucket.create_s3_bucket[each.key].arn,
          "${aws_s3_bucket.create_s3_bucket[each.key].arn}/*",
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      },
    ]
  })
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  for_each = local.buckets
  bucket = aws_s3_bucket.create_s3_bucket[each.key].id
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "bucket-public-access-block" {
  for_each = local.buckets
  bucket = aws_s3_bucket.create_s3_bucket[each.key].id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}