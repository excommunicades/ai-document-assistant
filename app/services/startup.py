import uuid

from app.config import settings
from app.services.chunk_handler import chunk_text
from app.db.weavite_db import connect_weaviate
from app.services.embedding import generate_embeddings
from app.db.weavite_utils import create_collection, save_embedding
from app.services.file_handler import get_txt_files_content


def process_and_store_documents():

    client = None

    try:
        client = connect_weaviate()
        exists = client.collections.exists(settings.weaviate_class_name)
        if exists:
            print(f"Collection '{settings.weaviate_class_name}' already exists")
            return
        else:
            print('Creating')
            create_collection(settings.weaviate_class_name)
    except Exception:
        pass
    finally:
        if client:
            client.close()

    try:
        docs = get_txt_files_content()
        if not docs:
            print("⚠️ No documents found.")
            return
    except Exception as e:
        print(f"❌ Error reading documents: {e}")
        return

    for doc_index, doc_text in enumerate(docs, start=1):
        chunks = chunk_text(doc_text)

        embeddings = generate_embeddings(chunks)

        for chunk, embedding in zip(chunks, embeddings):
            try:
                save_embedding(chunk, embedding, object_id=str(uuid.uuid4()))
            except Exception as e:
                print(f"❌ Failed to save chunk: {e}")

    print("✅ Document ingestion complete.")
