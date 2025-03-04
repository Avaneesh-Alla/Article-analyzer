# Article Analysis Tool with Generative AI

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00ADD8?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

A generative AI-powered tool for analyzing and questioning content from online articles. Converts web content into vector embeddings using FAISS and OpenAI, enabling semantic search and AI-powered question answering.

## Features

- **URL Processing**: Accepts multiple URLs as input sources
- **Vector Conversion**: Transforms content into embeddings using OpenAI's models
- **FAISS Integration**: Efficient vector similarity search and storage
- **AI-Powered Q&A**: Utilizes GPT-4 for contextual question answering
- **Source Tracking**: Displays original sources of information for answers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/article-analysis-tool.git
cd article-analysis-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```
## Requirements
1. Python 3.8+
2. Streamlit
3. LangChain
4. FAISS (CPU)
5. OpenAI
6. Unstructured
7. python-dotenv

## Usage
#### Start the application
```bash
streamlit run main.py
```
#### In the sidebar:
1. Enter up to 3 valid URLs
2. Click "Process URLs"
#### Once processing completes:
1. Enter your question in the main input field
2. Receive AI-generated answers with source references

## How it works
#### Content Ingestion:
1. URL content is loaded using UnstructuredURLLoader
2. Text is split into chunks using recursive character splitting

#### Vector Processing:
1. OpenAI embeddings convert text to vectors
2. FAISS stores vectors for efficient similarity search

#### Query Handling:
1. Semantic search finds relevant content chunks
2. GPT-4 generates answers based on context

## Acknowledgement

1. LangChain for LLM orchestration
2. OpenAI for embedding models and GPT-4
3. FAISS for efficient similarity search
4. Streamlit for intuitive web interface
