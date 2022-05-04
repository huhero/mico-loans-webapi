# FastApi
from fastapi import HTTPException

# aws
import boto3

# utils
from decouple import config


class S3Service:
    def __init__(self):
        self.key = config("AWS_ACCESS_KEY")
        self.secret = config("AWS_SECRET_KEY")
        self.s3 = boto3.client(
            "s3", aws_access_key_id=self.key, aws_secret_access_key=self.secret
        )
        self.bucket = config("AWS_BUCKET_NAME")
        self.region = config("AWS_REGION")

    def upload(self, path, key):
        try:

            self.s3.upload_file(
                path,
                self.bucket,
                key,
                ExtraArgs={"ACL": "public-read", "ContentType": f"application/pdf"},
            )
            return f"https://{self.bucket}.s3.amazonaws.com/{key}"
        except Exception as ex:
            raise HTTPException(500, "S3 is not available")
