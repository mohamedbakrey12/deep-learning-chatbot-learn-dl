import os
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


def load_llm():
    return Ollama(
        model="llama3.1",  # تأكد أنه مكتوب تمامًا كما يظهر في ollama list
        temperature=0.1,
        base_url="http://host.docker.internal:11434"  # Ollama with Docker

    )
def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )


if __name__ == "__main__":
    embedding = load_embedding_model()
    vectorstore = FAISS.load_local("faiss_store", embedding, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever()

    llm = load_llm()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    while True:
        question = input("\n❓ سؤالك: ")
        if question.lower() in ["exit", "quit"]:
            break
        result = qa_chain.run(question)
        print("🤖 Result\n", result)
