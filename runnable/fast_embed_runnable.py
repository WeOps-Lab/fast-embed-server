from typing import List

from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_core.runnables import RunnableLambda

from core.server_settings import server_settings


class FastEmbedRunnable:
    def __init__(self):
        self.embedding = FastEmbedEmbeddings(model_name=server_settings.model_name, cache_dir="models")

    def instance(self):
        return RunnableLambda(self.execute).with_types(input_type=str, output_type=List[float])

    def execute(self, text: str) -> List[float]:
        return self.embedding.embed_query(text)
