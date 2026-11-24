# 📄 RAG Document Question Answering

## 📌 Project Overview

RAG (Retrieval-Augmented Generation) Document Question Answering is an AI-powered application that allows users to upload PDF or TXT documents and ask questions based on their content.

The application uses **LangChain, ChromaDB, Hugging Face Embeddings, and Groq LLM** to retrieve relevant information from uploaded documents and generate accurate, context-based answers.

It follows a Retrieval-Augmented Generation (RAG) approach, ensuring that responses are generated using the information available in the uploaded document rather than relying on external knowledge.

## ✨ Features

- **Document Upload:** Upload PDF and TXT files through an interactive Streamlit interface.
- **Text Extraction:** Extracts content from uploaded documents using LangChain document loaders.
- **Text Chunking:** Splits documents into smaller chunks using RecursiveCharacterTextSplitter.
- **Embedding Generation:** Converts text chunks into numerical embeddings using the Hugging Face Sentence Transformer model.
- **Vector Storage:** Stores document embeddings in ChromaDB for efficient similarity-based retrieval.
- **Context Retrieval:** Uses Maximum Marginal Relevance (MMR) to retrieve relevant and diverse document chunks.
- **AI-Powered Answers:** Uses Groq LLM to generate answers based on the retrieved document context.
- **Context-Based Responses:** Restricts answers to the uploaded document and avoids unsupported information.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | RAG pipeline orchestration |
| ChromaDB | Vector database |
| Hugging Face Embeddings | Text embedding generation |
| Sentence Transformers | Embedding model |
| Groq API | LLM inference |
| PyPDFLoader | PDF document loading |
| TextLoader | TXT document loading |

### AI Models

- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Language Model:** `openai/gpt-oss-20b` (via Groq)

## ⚙️ How It Works

The application follows these steps:

1. **Upload Document:** The user uploads a PDF or TXT file.
2. **Load Document:** LangChain extracts the document content.
3. **Split Text:** The extracted text is divided into chunks using a chunk size of 1200 characters and an overlap of 200 characters.
4. **Generate Embeddings:** Hugging Face converts the text chunks into vector embeddings.
5. **Store Vectors:** ChromaDB stores the embeddings for retrieval.
6. **Retrieve Context:** The MMR retrieval method identifies relevant document chunks for the user's question.
7. **Generate Answer:** Groq LLM receives the retrieved context and question to generate a response.
8. **Display Result:** Streamlit displays the generated answer to the user.

## 🔄 RAG Architecture

```text
        PDF / TXT Document
                |
                v
        Document Loading
                |
                v
          Text Splitting
                |
                v
       Hugging Face Embeddings
                |
                v
           ChromaDB
          (Vector Store)
                |
                v
        User's Question
                |
                v
       MMR-Based Retrieval
                |
                v
       Relevant Document
             Context
                |
                v
           Groq LLM
                |
                v
       Context-Based Answer
                |
                v
        Streamlit Interface
```

## 📂 Project Structure

```text
RAG-Document-Question-Answering/
│
├── rag.py
├── .gitignore
└── README.md
```

## 📦 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lakshanika1/RAG-Document-Question-Answering.git
```

### 2. Navigate to the Project Directory

```bash
cd RAG-Document-Question-Answering
```

### 3. Install Required Dependencies

```bash
pip install streamlit langchain langchain-community langchain-text-splitters langchain-huggingface langchain-groq chromadb sentence-transformers pypdf
```

### 4. Configure the Groq API Key

Obtain an API key from the Groq Developer Console:

https://console.groq.com/

Set the API key as an environment variable.

**Windows (Command Prompt):**

```bash
set GROQ_API_KEY=your_groq_api_key
```

**Windows (PowerShell):**

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

**Linux / macOS:**

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Replace `your_groq_api_key` with your actual Groq API key.

Do not hardcode or upload API keys to GitHub.

### 5. Run the Application

```bash
streamlit run rag.py
```

The application will open in your default web browser.

## 🚀 How to Use

1. Launch the application using Streamlit.
2. Upload a PDF or TXT document.
3. Wait for the document processing to complete.
4. Enter a question related to the uploaded document.
5. Click the input field and enter your question.
6. View the AI-generated answer based on the document content.

## 🔍 Retrieval Configuration

The application uses the following configurations:

| Parameter | Value |
|---|---|
| Chunk Size | 1200 |
| Chunk Overlap | 200 |
| Retrieval Method | MMR |
| Number of Retrieved Chunks (k) | 8 |
| Fetch Size (fetch_k) | 20 |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM Temperature | 0 |

## 🎯 Applications

- Document-based question answering
- Research paper analysis
- Educational document assistance
- Business document analysis
- Information retrieval from PDF files
- Quick access to information in text documents

## 🔮 Future Enhancements

- Support for multiple document uploads.
- Chat history and conversational question answering.
- Display relevant source pages and retrieved passages.
- Persistent vector database storage.
- Improved document processing and error handling.
- Deployment as a cloud-based application.

## 📝 Conclusion

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system for document-based question answering.

By integrating LangChain, ChromaDB, Hugging Face Embeddings, and Groq LLM, the application retrieves relevant information from uploaded documents and generates concise, context-based answers.

It provides practical experience in **Large Language Models (LLMs), semantic search, vector databases, embeddings, and RAG pipeline development**.

## 👩‍💻 Author

**Lakshanika A P**

B.E. Computer Science and Engineering

---

⭐ If you find this project useful, consider giving the repository a star!
