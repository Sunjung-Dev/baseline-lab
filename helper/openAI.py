from openai import AsyncOpenAI
from settings import settings


class OpenAiHelper:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def upload_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return await self.client.files.create(file=file, purpose="assistants")
        
    async def upload_file_to_vector_store(self, file_id: str, vector_store_id: str):
        return await self.client.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_id,
        )

    async def get_file_list(self):
        return await self.client.files.list()

    async def get_file(self, file_id: str):
        return await self.client.files.retrieve(file_id)

    async def delete_file(self, file_id: str):
        return await self.client.files.delete(file_id)
   

