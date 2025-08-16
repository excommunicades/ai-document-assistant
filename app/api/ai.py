from langchain_ollama import OllamaLLM

from fastapi import APIRouter

from app.config import settings
from app.api.schemas.ai_schemas import PromptRequest
from app.db.weavite_utils import search_embedding
from app.services.embedding import generate_embeddings


ai_router = APIRouter(prefix="/ai", tags=["AI"])


@ai_router.post("/prompt")
async def handle_prompt(req: PromptRequest):
    embedding = generate_embeddings([req.prompt])[0]

    chunks = search_embedding(embedding, top_k=5, min_score=0.75)

    context = "\n".join([chunk["text"] for chunk in chunks])

    rag_prompt = f"""
    You are an AI assistant answering based only on the provided documents.
    If the answer is not found in them, respond: "I don't know the answer to this question."

    Context:
    {context}

    Question:
    {req.prompt}
    """

    llm = OllamaLLM(model=settings.llm_model, base_url=settings.ollama_api)
    answer = llm.invoke(input=rag_prompt).strip()

    return {"answer": answer}
