import streamlit as st
import os
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


# ========== إعداد الصفحة ==========
st.set_page_config(page_title="🤖 Helper to learn Deep Learning", layout="wide")

# ========== الشريط الجانبي ==========
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Deep_learning.png", width=250)
    st.markdown("## عن التطبيق")
    st.markdown("""
    This application is designed to help you learn about Deep Learning by answering your questions using a combination of a local LLM and a vector store for efficient retrieval of relevant information.    
    - ✅Work by using `llama3.1` as the LLM
    - ✅ Using `HuggingFaceEmbeddings` for text embeddings
    - ✅ Using FAISS as a vector store for efficient retrieval
    """)
    st.markdown("### 👨‍💻Developer:[@Mohamed Bakrey](https://github.com/mohamedbakrey12)")
    st.markdown("---")
    if st.button("🔄 إعادة تعيين المحادثة"):
        st.session_state.chat_history = []
        st.experimental_rerun()

# ========== العنوان ==========
st.markdown("<h1 style='text-align: center; color: #green;'>💡 Helper to learn Deep Learning</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask any question on Deep learning.</p>", unsafe_allow_html=True)
st.markdown("---")

# ========== تحميل النماذج ==========
@st.cache_resource
def load_llm():
    return Ollama(model="llama3.1", temperature=0.1)

@st.cache_resource
def load_retriever():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectorstore = FAISS.load_local("faiss_store", embedding, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()

llm = load_llm()
retriever = load_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# ========== تخزين المحادثة ==========
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ========== واجهة الإدخال ==========
with st.container():
    st.markdown("### 🗨️ Ask now:")
    user_input = st.text_input("✏️ Write youe question here:", key="input")

    if user_input:
        answer = qa_chain.run(user_input)
        st.session_state.chat_history.append({"question": user_input, "answer": answer})

# ========== عرض المحادثة ==========
if st.session_state.chat_history:
    st.markdown("## 📜History of chats")
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        st.markdown(f"""
        <div style="background-color:#green;padding:15px;border-radius:10px;margin-bottom:10px;">
            <b>🧑‍🎓 Question? </b> {chat['question']}<br><br>
            <b>🤖 Result: </b> {chat['answer']}
        </div>
        """, unsafe_allow_html=True)
