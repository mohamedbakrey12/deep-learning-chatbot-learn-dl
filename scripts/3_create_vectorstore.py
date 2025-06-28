import pickle
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

def load_chunks(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read().split("\n\n---\n\n")

if __name__ == "__main__":
    chunks = load_chunks("scripts/chunks.txt")
    embedding = load_embedding_model()
    
    vectorstore = FAISS.from_texts(chunks, embedding)
    vectorstore.save_local("faiss_store")

    print("✅ تم إنشاء قاعدة FAISS بنجاح")
