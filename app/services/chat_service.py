from app.services.vector_store import similarity_search
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

SYSTEM_PROMPT = """
You are an AI assistant answering questions strictly based on the provided context.
If the answer is not in the context, say "I don't know".
Do NOT make up information.
"""

def chat_with_documents(query: str) -> str:
    docs = similarity_search(query, k=8)

    if not docs:
        return "I don't know."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{query}

Answer:
"""

    return llm(prompt)
