from typing import List

from app.config import settings


def chunk_text(text: str) -> list[str]:

    lines = text.splitlines()
    chunks = []
    current_chunk = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
            continue

        current_chunk.append(stripped)

        if stripped.startswith("Question:") and current_chunk:
            if len(current_chunk) > 1:
                chunks.append(" ".join(current_chunk[:-1]))
                current_chunk = current_chunk[-1:]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
