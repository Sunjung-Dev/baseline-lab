import boto3
from settings import settings

class S3Helper:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        
    async def get_list_objects(self, prefix: str):
        continuation_token = None
        all_keys = []

        while True:
            if continuation_token:
                response = self.s3_client.list_objects_v2(
                    Bucket=settings.AWS_BUCKET_NAME,
                    Prefix=prefix,
                    ContinuationToken=continuation_token
                )
            else:
                response = self.s3_client.list_objects_v2(
                    Bucket=settings.AWS_BUCKET_NAME,
                    Prefix=prefix
                )

            contents = response.get('Contents', [])
            for content in contents:
                all_keys.append(content.get("Key"))

            if response.get('IsTruncated'):  
                continuation_token = response.get('NextContinuationToken')
            else:
                break
            
        return all_keys
        
    async def get_document(self, key_name: str):
        response = self.s3_client.get_object(Bucket=settings.AWS_BUCKET_NAME, Key=key_name)
        return response.get("Body").read().decode("utf-8")

