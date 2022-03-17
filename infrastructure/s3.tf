resource "aws_s3_bucket" "dl" {
  # parâmetros de configuração do recurso escolhido
  bucket = "edc-desafio-mod1-helton-tf"

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_acl" "dl" {
  bucket = aws_s3_bucket.dl.id
  acl    = "private"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "dl" {
  bucket = aws_s3_bucket.dl.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}