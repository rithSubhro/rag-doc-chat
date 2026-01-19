from fastapi import APIRouter
from app.services.llm_service import get_llm_response

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "Backend is running"}

@router.get("/llm-test")
def llm_test():
    response = get_llm_response(
        "Explain Retrieval Augmented Generation in 2 lines."
    )
    return {"llm_response": response}
