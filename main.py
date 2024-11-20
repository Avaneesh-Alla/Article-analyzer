import os
import streamlit as st
import pickle
import time
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)

st.title("Article Analysis Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
n = 3
for i in range(n):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()

# OpenAI configuration
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai_chat(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or another supported chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following context, answer the question: {question}\n\nContext:\n{context}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message['content']

if process_url_clicked:
    # Load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # Create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            # Use FAISS to perform a similarity search
            results = vectorstore.similarity_search(query)
            # Combine the content of the relevant documents into a context
            context = "\n".join([doc.page_content for doc in results])
            # Use OpenAI chat model to generate a response
            answer = ask_openai_chat(query, context)
            st.header("Answer")
            st.write(answer)

            # Display sources, if available
            sources = "\n".join([doc.metadata.get("source", "") for doc in results])
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)
