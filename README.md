# 🎥 YouTube Chatbot RAG-based Project

This project is a **Retrieval-Augmented Generation (RAG)** based chatbot built in **Google Colab**. It enables users to ask questions about any YouTube video by extracting its transcript, indexing it using FAISS, and generating answers using LLMs **OpenAI GPT**.

The notebook implements each component separately for better understanding — from transcript extraction to generation — following a modular design in **code cells**.

---

##  Key Features

-  Built entirely in **Google Colab**
-  Fetches **YouTube transcripts** using `youtube-transcript-api`
-  Splits long transcripts into **chunks** for efficient retrieval
-  Creates **vector embeddings** using `sentence-transformers`
-  Uses **FAISS** for similarity search
-  Retrieves relevant chunks and passes them to an **LLM for generation**
-  Provides human-like responses from video content
-  Each RAG step is implemented in **individual code cells**

---

##  Notebook Workflow

1. **Setup and Install Dependencies**
2. **Extract Transcript from YouTube Video**
3. **Clean and Chunk the Transcript**
4. **Embed Chunks using Sentence Transformers**
5. **Store Embeddings in FAISS Vector Store**
6. **User Query Input**
7. **Retrieve Relevant Chunks**
8. **Generate Final Answer using LLM**
