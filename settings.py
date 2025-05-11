import os


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or ""
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") or ""
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY") or ""
    AWS_REGION = os.getenv("AWS_REGION") or ""
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME") or ""
    AWS_DIRECTORY = os.getenv("AWS_DIRECTORY") or ""
    
    SITEMAP_VECTOR_STORE_ID = os.getenv("SITEMAP_VECTOR_STORE_ID") or ""
    LAWS_REGULATIONS_VECTOR_STORE_ID = os.getenv("LAWS_REGULATIONS_VECTOR_STORE_ID") or ""

settings = Settings()
