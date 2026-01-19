import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.core.security.jwt import get_current_user
from app.db.database import SessionLocal
from app.models.document import Document
from app.models.user import User

from app.services.document_parser import extract_text_from_pdf
from app.services.text_chunker import chunk_text
from app.models.chunk import DocumentChunk
from app.services.vector_store import add_texts_to_vector_store



UPLOAD_DIR = "uploads"

router = APIRouter(prefix="/documents", tags=["documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    file_location = f"{UPLOAD_DIR}/{current_user.id}_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        filename=file.filename,
        file_path=file_location,
        owner_id=current_user.id
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    text = extract_text_from_pdf(file_location)

    chunks = chunk_text(text)

    for chunk in chunks:
        db_chunk = DocumentChunk(
            content=chunk,
            document_id=document.id,
            owner_id=current_user.id
        )
        db.add(db_chunk)

    add_texts_to_vector_store(chunks)

    db.commit()

    return {
        "message": "Document uploaded and processed",
        "document_id": document.id,
        "chunks_created": len(chunks)
    }
