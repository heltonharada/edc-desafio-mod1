resource "aws_s3_object" "codigo_spark" {
  # bucket = aws_s3_bucket.datalake.id
  bucket = aws_s3_bucket.dl.id

  key    = "emr-code/pyspark/job_spark.py"
  acl    = "private"
  source = "../etl/job_spark.py"
  etag   = filemd5("../etl/job_spark.py")

}