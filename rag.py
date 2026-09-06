import streamlit as st
import os
import tempfile
import chromadb

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# ================================
# Page Config
# ================================
st.set_page_config(page_title="RAG App", layout="wide")
st.title("📄 RAG Document Question Answering")


# ================================
# Upload File
# ================================
uploaded_file = st.file_uploader(
    "Upload a PDF or TXT document",
    type=["pdf", "txt"]
)


if uploaded_file is not None:

    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("Document uploaded successfully!")

    # ================================
    # Load Document
    # ================================
    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    documents = loader.load()

    # ================================
    # Split Text
    # ================================
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200
    )

    split_documents = text_splitter.split_documents(documents)

    # ================================
    # Create Embeddings
    # ================================
    embeddings_model = HuggingFaceEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )

    # ================================
    # Create Vector Store
    # ================================
    client = chromadb.Client()

    vector_store = Chroma.from_documents(
        documents=split_documents,
        embedding=embeddings_model,
        client=client
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
           "k": 8,
           "fetch_k": 20
        }
    )

    # ================================
    # Setup LLM
    # ================================
    groq_api_key=os.getenv("GROQ_API_KEY")
    llm = ChatGroq(
        model_name="openai/gpt-oss-20b",
        temperature=0,
        groq_api_key=groq_api_key
    )

    prompt_template = ChatPromptTemplate.from_template(
    """
You are a document question-answering assistant.

Answer the question ONLY using the information provided in the context.

Rules:
1. Do not use outside knowledge.
2. Do not guess or make up information.
3. If the answer is not clearly present in the context, say:
   "The information is not available in the document."
4. Give a direct and accurate answer.
5. Keep the answer concise.
6. If the context contains multiple relevant points, include all of them.

Context:
{context}

Question:
{input}

Answer:
"""
)

    def format_docs(docs):
        return "\n\n".join(
           f"Page {doc.metadata.get('page', 'unknown')}:\n{doc.page_content}"
           for doc in docs
        )

    rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | prompt_template
    | llm
    | StrOutputParser()
    )

    # ================================
    # Ask Question
    # ================================
    query = st.text_input("Ask a question about the document")

    if query:
        with st.spinner("Generating answer..."):
            response = rag_chain.invoke(query)

        st.subheader("Answer:")
        st.write(response)