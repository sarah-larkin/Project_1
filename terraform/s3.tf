#ingestion bucket for raw data
resource "aws_s3_bucket" "ingestion_bucket" {
  bucket_prefix = var.S3_ingestion_prefix

  tags = {
    Name        = "ingestion bucket"
    Environment = var.environment
  }
}

#processed bucket for cleaned data
resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = var.S3_processed_prefix

  tags = {
    Name        = "processed bucket"
    Environment = var.environment
  }
}