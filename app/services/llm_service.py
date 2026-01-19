from langchain_community.llms import Ollama
from app.core.config import settings

def get_llm_response(prompt: str) -> str:
    llm = Ollama(model=settings.LLM_MODEL)
    return llm(prompt)
