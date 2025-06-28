* ✅ **Streamlit app**

* ✅  **RAG (Retrieval-Augmented Generation)**
* ✅  **Source data Deep Learning book** 

`README.md`

---

## 📄 `README.md` 
````markdown
# 💡 Deep Learning RAG Assistant

An interactive AI assistant for learning Deep Learning using Retrieval-Augmented Generation (RAG) and a local language model (LLaMA 3.1 via Ollama). This assistant can answer questions from a vectorized Deep Learning book in real time using a combination of FAISS retrieval and local LLM.

---

## 🚀 Features

- ✅ Powered by **RAG**: Combines semantic search + generative response
- ✅ Uses a **local Ollama model** (`llama3.1`)
- ✅ Answers based on content from a **Deep Learning textbook**
- ✅ Built with **LangChain** + **FAISS** + **Streamlit**
- ✅ Fully containerized using **Docker**
- ✅ Clean and interactive chat UI with **chat history**

---

## 📚 Data Source

The assistant is built using a vectorized version of a Deep Learning book (in English). Embeddings were generated using `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` and stored in a FAISS vectorstore.

---

## 🖥️ Demo UI

![screenshot](screenshot.png)

---

## 🧪 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/deep-learning-rag-arabic.git
cd deep-learning-rag-arabic
````

### 2. Run with Docker

```bash
docker build -t deep-learning-rag .
docker run -p 8501:8501 deep-learning-rag
```

> 💡 Make sure [Ollama](https://ollama.com/) is installed and `llama3.1` is downloaded:

```bash
ollama run llama3.1
```

---

## ⚙️ Project Structure

```
.
├── app.py                    # Streamlit interface
├── faiss_store/              # Preprocessed FAISS index + metadata
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## 🔍 Tech Stack

* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Ollama](https://ollama.com/)
* [HuggingFace Sentence Transformers](https://www.sbert.net/)

---

## 📌 Author

Developed by [Mohamed Bakrey Mahmoud](https://github.com/mohamedbakrey12) – AI Developer passionate about educational LLMs.

---

## 📄 License

MIT License. Free to use and modify.
