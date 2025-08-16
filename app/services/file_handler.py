import os
from typing import List

from app.config import settings


def get_txt_files_content() -> List[str]:

    docs_dir = settings.docs_path
    texts = []

    if not os.path.isdir(docs_dir):
        raise FileNotFoundError(f"Docs directory not found: {docs_dir}")

    for filename in os.listdir(docs_dir):
        if filename.lower().endswith(".txt"):
            file_path = os.path.join(docs_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    texts.append(f.read())
            except UnicodeDecodeError:
                with open(file_path, "r", encoding="latin-1") as f:
                    texts.append(f.read())

    return texts
