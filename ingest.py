from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load the PDF
print("📄 Loading document...")
loader = PyPDFLoader("data/my_document.pdf")
docs = loader.load()

# 2. Split into small chunks (so the AI doesn't get overwhelmed)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

# 3. Create Embeddings (Turn text into math)
# We use the 'nomic-embed-text' model you pulled earlier
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 4. Save to a local database folder called 'db'
print("🧠 Vectorizing and saving to local database...")
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings, 
    persist_directory="./db"
)

print("✅ Success! Your assistant now has a memory.")
