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
