import os
import streamlit as st

from read_pdf import extract_text
from chunking import create_chunks
from embeddings import embed_text, model
from vector_store import create_vector_store, search
from chatbot import ask_gemini

st.set_page_config(page_title="Retrieval Chatbot")

st.title(" Retrieval Chatbot 👽")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded")

    text = extract_text(path)

    chunks = create_chunks(text)

    embeddings = embed_text(chunks)

    index = create_vector_store(embeddings)

    question = st.text_input("Ask a Question")

    if question:

        query_embedding = model.encode(question)

        ids = search(index, query_embedding)

        context = ""

        for i in ids:
            context += chunks[i] + "\n"

        answer = ask_gemini(
            context,
            question
        )

        st.subheader("Answer")

        st.write(answer)