from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str
    app_debug: bool

    weaviate_url: str
    ollama_api: str
    docs_path: str
    weaviate_class_name: str
    llm_model: str

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
