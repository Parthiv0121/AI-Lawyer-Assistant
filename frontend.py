import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone

# ======================================================
# Load Environment Variables
# ======================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

INDEX_NAME = "ailawyer-384"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.1-8b-instant"

# ======================================================
# Streamlit UI
# ======================================================

st.set_page_config(
    page_title="AI Lawyer Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ AI Lawyer Assistant")
st.write("Ask legal questions based on the uploaded legal documents.")

# ======================================================
# Prompt
# ======================================================

SYSTEM_PROMPT = """
You are an AI Lawyer Assistant.

Answer ONLY from the retrieved legal documents.

Rules:

1. Use only the retrieved context.

2. Never make up legal information.

3. If the answer is unavailable, say:

"I don't know based on the uploaded legal documents."

4. Do not provide personal legal advice.

5. If the question is unrelated to law, respond:

"I can only answer questions from the uploaded legal documents."

Retrieved Context:
{context}

Question:
{input}

Answer:
"""

# ======================================================
# Helper Function
# ======================================================

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# ======================================================
# Load RAG
# ======================================================

@st.cache_resource(show_spinner="Loading Legal Knowledge Base...")
def load_rag():

    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY missing in .env")

    if not PINECONE_API_KEY:
        raise RuntimeError("PINECONE_API_KEY missing in .env")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    index = pc.Index(INDEX_NAME)

    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("user", "{input}")
        ]
    )

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=LLM_MODEL,
        temperature=0.3,
        max_tokens=700
    )

    chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

# ======================================================
# Load Chain
# ======================================================

try:
    rag_chain = load_rag()

except Exception as e:
    st.error(e)
    st.stop()

# ======================================================
# Chat History
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ======================================================
# User Input
# ======================================================

question = st.chat_input("Ask your legal question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching legal documents..."):

            try:
                answer = rag_chain.invoke(question)

            except Exception as e:
                answer = f"Error: {e}"

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )