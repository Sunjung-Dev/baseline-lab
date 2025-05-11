import asyncio
from enum import Enum
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from settings import settings
from helper.s3 import S3Helper
from helper.openAI import OpenAiHelper


class DocumentsType(Enum):
    SITEMAP = "sitemap-general/"
    LAWS = "kicpa-laws-regulations/"

class UploadService:
    def __init__(self):
        self.openai_helper = OpenAiHelper()
        self.s3_helper = S3Helper()

    async def _fetch_objects_from_s3(self, key_name: str):
        objects = await self.s3_helper.get_list_objects(key_name)
        for object in objects:
            document = await self.s3_helper.get_document(object)

            with open(f"./s3_documents/{object}.txt", "w") as f:
                f.write(document)
      
    
    async def upload_s3_documents_to_vectorstore(self):
        """
        description:
            - fetch sitemap, laws from s3
            - upload to openai vector store
        """
        
        try:
            for root, _, files in os.walk("./s3_documents/sitemap-general"):
                for file in files:
                    full_path = os.path.join(root, file)
                    file_id = await self.openai_helper.upload_file(full_path)
                    await self.openai_helper.upload_file_to_vector_store(file_id.id, settings.SITEMAP_VECTOR_STORE_ID)
                    
            for root, _, files in os.walk("./s3_documents/kicpa-laws-regulations"):
                for file in files:
                    full_path = os.path.join(root, file)
                    file_id = await self.openai_helper.upload_file(full_path)
                    await self.openai_helper.upload_file_to_vector_store(file_id.id, settings.LAWS_REGULATIONS_VECTOR_STORE_ID)
                
            
        except Exception as e:
            print(e)
            raise e
        