import uuid
import weaviate
from typing import List
from weaviate.classes.query import MetadataQuery
from weaviate.classes.config import Property, DataType, Configure

from app.config import settings
from app.db.weavite_db import connect_weaviate


def create_collection(
            name: str,
            properties: list[Property] | None = None,
        ):
    client = None
    try:
        client = connect_weaviate()

        if properties is None:
            properties = [
                Property(
                    name="text",
                    data_type=DataType.TEXT,
                    skip_vectorization = True,
                ),
            ]
        if client.collections.exists(name):
            print(f"Collection already exists")
            return

        client.collections.create(
            name=name,
            properties=properties,
            generative_config=None,
        )
        print(f"Collection '{name}' created successfully.")

    except Exception as e:
        print(f"Error creating collection '{name}':", e)

    finally:
        if client:
            client.close()


def search_embedding(query_vector: List[float], top_k: int = 5, min_score: float = 0.75) -> List[str]:

    try:
        client = connect_weaviate()
        collection = client.collections.get(settings.weaviate_class_name)

        response = collection.query.near_vector(
            near_vector=query_vector,
            return_metadata=MetadataQuery(distance=True, certainty=True),
            limit=top_k
        )

        results = []
        for obj in response.objects:
            results.append({
                "text": obj.properties["text"],
                "distance": obj.metadata.distance,
                "certainty": obj.metadata.certainty
            })
        return results
    except Exception as e:
        print("Error during search:", e)
        return []
    finally:
        client.close()


def save_embedding(chunk_text: str, embedding: List[float], object_id: str = None) -> None:
    client = None
    try:
        client = connect_weaviate()

        if object_id is None:
            object_id = str(uuid.uuid4())

        data_object = {
            "text": chunk_text,
        }

        doc_collection = client.collections.get(settings.weaviate_class_name)
        token = doc_collection.data.insert(
            uuid=object_id,
            vector=embedding,
            properties=data_object
        )

    except Exception as e:
        print('An error occurred during save:', e)

    finally:
        if client:
            client.close()
