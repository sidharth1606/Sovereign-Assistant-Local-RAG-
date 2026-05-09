# 🛡️ SOVEREIGN-INTELLIGENCE: [COLLECTIVE_SUITE_V2.0]

> **CORE_MISSION:** Engineering private, autonomous, and local-first AI architectures.
> **STATUS:** `OPERATIONAL` | **ENCRYPTION:** `AES-256_LOCAL`

This suite contains two flagship autonomous systems designed for the 2027 enterprise landscape, focusing on data sovereignty and agentic task delegation.

---

## 📂 PROJECT_01: SOVEREIGN-RAG (Document Intelligence)
*The Single-Agent retrieval system for private document analysis.*

### ⚡ CORE_SPECS
*   **BRAIN:** `Llama 3.1:8b` via Ollama
*   **VECTOR_MATRIX:** `ChromaDB`
*   **CAPABILITY:** 100% Offline Semantic Search & Document Q&A
### Needed Packages
pip install streamlit langchain-ollama langchain-chroma pypdf langchain-text-splitters


### 🚀 BOOT_SEQUENCE
```powershell
# 1. Initialize Engines
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# 2. Start Assistant
python -m streamlit run ui_app.py





This is a breakdown of the project suite you've built, written in a way that explains the "What," "How," and "Why"—perfect for a portfolio or an interview.

🛡️ Project 1: Sovereign-RAG
What is it?
Sovereign-RAG is a Private Local Intelligence Engine. It allows you to talk to your PDF documents without ever sending that data to the internet. It uses Retrieval-Augmented Generation (RAG), which means the AI "reads" your specific files to give accurate answers instead of guessing.

What is happening under the hood?
Ingestion: When you upload a PDF, the system breaks it into small "chunks" of text.

Embedding: A model (nomic-embed-text) converts those text chunks into mathematical vectors.

Storage: These vectors are stored in ChromaDB, a local vector database.

Retrieval: When you ask a question, the system finds the most relevant math vectors in the database and sends that specific text to the Llama 3.1 model to generate an answer.

How to use it:
Open the dashboard and upload a PDF in the sidebar.

Click "Index Document" to let the AI "learn" the file.

Type any question about the document in the chat box.
