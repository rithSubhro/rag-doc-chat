# rag-doc-chat

# RAG Document Chat

A full-stack **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions about them using **LLMs grounded in their own data**.

The system parses documents, chunks and embeds text, performs semantic search using a vector database, and generates answers strictly from retrieved context to prevent hallucinations.

---

## 🚀 Features

- 🔐 **JWT-based authentication** (secure, multi-user)
- 📄 **Document upload** (PDF support)
- 🧠 **Text parsing & intelligent chunking**
- 🔎 **Semantic search** using vector embeddings (FAISS)
- 🤖 **RAG-based chat** with hallucination control
- 💾 **Persistent vector store** (survives server restarts)
- 🧩 **User-scoped data isolation**
- 🌐 **Angular frontend** for interaction

---

## 🏗️ Architecture Overview

User
└── Upload Document (PDF)
└── Text Extraction
└── Chunking
└── Embeddings (local model)
└── Vector Store (FAISS)
└── Semantic Retrieval
└── LLM Answer Generation (RAG)



The LLM **never answers from its own knowledge** — all responses are grounded in retrieved document context.

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **LangChain**
- **Ollama (local LLMs)**
- **FAISS** (vector database)
- **SQLAlchemy**
- **SQLite / PostgreSQL**
- **JWT Authentication**

### Frontend
- **Angular**
- **TypeScript**

### AI / GenAI
- Retrieval-Augmented Generation (RAG)
- Local embeddings (`nomic-embed-text`)
- Local LLM inference (`llama3`)
- Prompt grounding to prevent hallucinations


---

## 🔐 Authentication Flow

1. User registers / logs in
2. Backend issues a JWT
3. JWT is required for:
   - Document upload
   - Semantic search
   - Chat queries
4. All documents and embeddings are **scoped to the user**

---

## 🧠 How RAG Works Here

1. User uploads a document
2. Document is parsed and chunked
3. Chunks are embedded and stored in FAISS
4. User asks a question
5. Relevant chunks are retrieved via semantic search
6. LLM generates an answer **only from retrieved context**
7. If context is insufficient → `"I don't know"`

---

## ▶️ Running Locally

### Prerequisites
- Python 3.9+
- Ollama installed
- Node.js (for Angular)

### Backend
bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


🧪 Example API Usage
Chat with documents
POST /chat
{
  "query": "What is my experience with Python?"
}
Response:
{
  "query": "What is my experience with Python?",
  "answer": "You have experience using Python for backend development, APIs, and problem solving..."
}


🧩 Design Decisions

RAG instead of fine-tuning to keep data private and reduce cost

Local models to avoid paid APIs

Persistent vector storage for production realism

Strict grounding to prevent hallucinations

Minimal frontend to keep focus on GenAI backend

📌 Future Improvements

Streaming responses

Document deletion & re-indexing

Multi-file conversations

Evaluation metrics for answer relevance

Cloud deployment (GCP / Azure)


