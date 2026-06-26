# Royal Enfield AI Diagnostic Assistant (Local)

## What it does
Local RAG assistant for Royal Enfield motorcycles (v1):
- User chats with problem description
- Retrieval from local dataset stored in ChromaDB
- Gemini generates structured diagnosis/checks/solution strictly from retrieved context
- Chat history saved in SQLite

## Requirements
- Python 3.11+
- Windows 11
- Environment variable: `GEMINI_API_KEY`

## Setup
1) Create venv (project-local)
```bash
python -m venv venv
venv\Scripts\activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Set Gemini key
```bash
set GEMINI_API_KEY=your_key_here
```

## Run Backend
```bash
uvicorn backend.main:app --reload --port 8000
```

## Run Frontend (Streamlit)
```bash
streamlit run frontend/app.py --server.port 8501
```

## How to Use
1. Start the backend server (see "Run Backend" above)
2. In a new terminal, start the Streamlit frontend
3. Open browser to `http://localhost:8501`
4. Describe your Royal Enfield motorcycle issue
5. Get AI-generated diagnosis and solutions based on your knowledge base

## Project Structure
```
├── backend/
│   └── main.py          # FastAPI backend
├── frontend/
│   └── app.py           # Streamlit UI
├── knowledge_base/
│   └── royal_enfield_troubleshooting.csv  # RAG dataset
├── vector_db/           # ChromaDB persisted vectors
├── data/
│   └── royal_enfield.db # SQLite chat history
├── requirements.txt
└── README.md
```

## Notes
- Dataset: `knowledge_base/royal_enfield_troubleshooting.csv`
- Vector DB: persisted under `vector_db/`
- Chat history: stored in `data/royal_enfield.db`
