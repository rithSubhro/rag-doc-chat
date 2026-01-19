from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security.jwt import get_current_user
from app.services.chat_service import chat_with_documents

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    query: str

@router.post("/")
def chat(
    data: ChatRequest,
    current_user=Depends(get_current_user)
):
    answer = chat_with_documents(data.query)
    return {
        "query": data.query,
        "answer": answer
    }
