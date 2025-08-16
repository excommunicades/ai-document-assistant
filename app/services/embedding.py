from typing import List
from sentence_transformers import SentenceTransformer

from app.config import settings
from app.db.weavite_db import connect_weaviate


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def generate_embeddings(chunks: List[str]) -> List[List[float]]:

    if not chunks:
        return []

    embeddings = model.encode(chunks, convert_to_numpy=True).tolist()
    return embeddings
