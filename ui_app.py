import streamlit as st
import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Sovereign Assistant", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #e0e0e0; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Sovereign Assistant")
st.caption("2027 Local RAG Interface | Windows-Stable Version")
st.markdown("---")

# --- 2. CACHED MODELS ---
@st.cache_resource
def get_models():
    llm = OllamaLLM(model="llama3.1:8b")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return llm, embeddings

llm, embeddings = get_models()

# --- 3. SIDEBAR: DATA MANAGEMENT ---
with st.sidebar:
    st.header("📂 Knowledge Base")
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_file:
        if st.button("🚀 Index Document"):
            with st.spinner("Processing..."):
                temp_path = "temp_upload.pdf"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                try:
                    loader = PyPDFLoader(temp_path)
                    docs = loader.load()
                    
                    if docs:
                        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                        chunks = splitter.split_documents(docs)
                        
                        # WINDOWS FIX: Don't delete the folder. Just add to it.
                        # ChromaDB handles the update internally without locking errors.
                        vector_db = Chroma.from_documents(
                            documents=chunks, 
                            embedding=embeddings, 
                            persist_directory="./db"
                        )
                        st.success(f"✅ Indexed {len(chunks)} sections.")
                    else:
                        st.error("❌ PDF is unreadable.")
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

    st.markdown("---")
    # WINDOWS FIX: Internal delete instead of os.remove to avoid WinError 32
    if st.button("🗑️ Reset Assistant Memory"):
        if os.path.exists("./db"):
            try:
                db_to_clear = Chroma(persist_directory="./db", embedding_function=embeddings)
                all_ids = db_to_clear.get()['ids']
                if all_ids:
                    db_to_clear.delete(ids=all_ids)
                    st.toast("Internal database wiped!")
                else:
                    st.info("Database is already empty.")
                st.rerun()
            except Exception as e:
                st.error(f"File Lock Error: {e}. Please restart the app to clear files manually.")
        else:
            st.info("No memory found.")

# --- 4. CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt_text := st.chat_input("Ask about your document..."):
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    with st.chat_message("user"):
        st.markdown(prompt_text)

    with st.chat_message("assistant"):
        if os.path.exists("./db"):
            # Connect and Retrieve
            db = Chroma(persist_directory="./db", embedding_function=embeddings)
            
            # Check if DB actually has data
            if len(db.get()['ids']) > 0:
                retriever = db.as_retriever(search_kwargs={"k": 3})
                
                template = """Use this context to answer:
                Context: {context}
                Question: {question}
                Answer:"""
                
                rag_prompt = ChatPromptTemplate.from_template(template)
                
                chain = (
                    {"context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)), 
                     "question": RunnablePassthrough()}
                    | rag_prompt | llm | StrOutputParser()
                )
                
                response = chain.invoke(prompt_text)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.warning("The database is empty. Please Index a document first.")
        else:
            st.warning("Please upload and Index a PDF first.")
