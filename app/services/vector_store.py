import os
from langchain_community.vectorstores import FAISS
from app.services.embedding_service import get_embedding_function

VECTOR_DIR = "vector_store"
vector_store = None

def load_vector_store():
    global vector_store
    if os.path.exists(VECTOR_DIR):
        embeddings = get_embedding_function()
        vector_store = FAISS.load_local(VECTOR_DIR, embeddings)
    return vector_store

def save_vector_store():
    if vector_store:
        vector_store.save_local(VECTOR_DIR)

def add_texts_to_vector_store(texts: list[str]):
    global vector_store
    embeddings = get_embedding_function()

    if vector_store is None:
        vector_store = FAISS.from_texts(texts, embeddings)
    else:
        vector_store.add_texts(texts)

    save_vector_store()

def similarity_search(query: str, k: int = 8):
    if vector_store is None:
        load_vector_store()
    if vector_store is None:
        return []
    return vector_store.similarity_search(query, k=k)
