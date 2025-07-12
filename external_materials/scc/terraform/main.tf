# Terraform configuration for AWS DynamoDB table for LlamaIndex

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to deploy resources in"
  default     = "us-east-1"
}

variable "table_name" {
  description = "Name of the DynamoDB table for LlamaIndex storage"
  default     = "llamaindex_scc"
}

resource "aws_dynamodb_table" "llamaindex_scc" {
  name           = var.table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "PK"
  range_key      = "SK"

  attribute {
    name = "PK"
    type = "S"
  }
  attribute {
    name = "SK"
    type = "S"
  }

  tags = {
    Name        = var.table_name
    Environment = "dev"
  }
}
