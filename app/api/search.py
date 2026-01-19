from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security.jwt import get_current_user
from app.services.vector_store import similarity_search

router = APIRouter(prefix="/search", tags=["search"])

class SearchRequest(BaseModel):
    query: str

@router.post("/")
def semantic_search(
    data: SearchRequest,
    current_user=Depends(get_current_user)
):
    results = similarity_search(data.query, k=8)

    return {
        "query": data.query,
        "results": [doc.page_content for doc in results]
    }
