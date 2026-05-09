import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Load models
llm = OllamaLLM(model="llama3.1:8b")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 2. Connect to database
vector_db = Chroma(persist_directory="./db", embedding_function=embeddings)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# 3. Create the modern RAG Chain (No 'langchain.chains' needed!)
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# This is the "Pipe" logic (|) that replaces the old RetrievalQA
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def start_chat():
    print("\n--- 🛡️ Sovereign Assistant: Modern RAG Active ---")
    while True:
        query = input("\nQuestion: ")
        if query.lower() == 'exit': break
        print("\n🔎 Searching...")
        response = rag_chain.invoke(query)
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    start_chat()
