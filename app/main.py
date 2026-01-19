from fastapi import FastAPI
from langchain_community.llms import Ollama
from app.api.health import router as health_router
from app.api.auth.routes import router as auth_router
from app.api.users import router as users_router
from app.db.database import Base, engine
from app.core.config import settings
from app.models.user import User
from app.models.document import Document
from app.api.documents import router as document_router
from app.models.chunk import DocumentChunk
from app.api.search import router as search_router
from app.api.chat import router as chat_router


app = FastAPI(title="Enterprise AI Assistant")

app.include_router(health_router)
app.include_router(document_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(search_router)
app.include_router(chat_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "Backend is running"}

@app.get("/llm-test")
def llm_test():
    llm = Ollama(model="llama3")
    response = llm("Explain what Retrieval Augmented Generation is in 2 lines.")
    return {
        "llm_response": response
    }
