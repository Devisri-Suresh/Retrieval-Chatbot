# 📄 Retrieval Chatbot

An AI-powered chatbot that answers questions from uploaded PDF documents using Retrieval-Augmented Generation (RAG). The application extracts text from PDFs, creates semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant content for a user's query, and generates context-aware responses using a Large Language Model (LLM).

---

## 🚀 Features

* Upload PDF documents
* Extract text from PDFs
* Split text into manageable chunks
* Generate sentence embeddings
* Store embeddings in a FAISS vector database
* Perform semantic similarity search
* Answer questions using retrieved document context
* Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* PyPDF2
* Sentence Transformers
* FAISS
* Google Gemini API
* NumPy

---

## 📂 Project Structure

```text
retrieval_chatbot/
│── app.py
│── read_pdf.py
│── chunking.py
│── embeddings.py
│── vector_store.py
│── chatbot.py
│── requirements.txt
│── .env
└── uploads/
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone <repository-url>
cd retrieval_chatbot
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key

```env
GEMINI_API_KEY=your_api_key_here
```

4. Run the application

```bash
streamlit run app.py
```

---

## ▶️ Usage

1. Launch the Streamlit application.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter your question in the chat interface.
5. Receive an answer generated from the most relevant document content.

---

## 📌 Applications

* Document Question Answering
* Research Assistance
* Educational Learning
* Knowledge Management
* Technical Documentation Search

---

## 📄 License

This project is intended for educational and learning purposes.
