# ⚖️ AI Lawyer Assistant

An AI-powered **Lawyer Assistant** built using **Python, LangChain, Pinecone, Hugging Face Embeddings, Groq LLM, and Streamlit**. This project leverages **Retrieval-Augmented Generation (RAG)** to answer legal questions based on uploaded legal documents.

---

## 📌 Features

* 📄 Answer legal questions using Retrieval-Augmented Generation (RAG)
* 🧠 Semantic search with Pinecone Vector Database
* 🤖 Fast responses using Groq LLM
* 🔎 Context-aware document retrieval using LangChain
* 💬 Interactive chat interface built with Streamlit
* 📚 Uses Hugging Face sentence-transformer embeddings
* ⚡ Real-time legal document search and question answering

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Pinecone Vector Database
* Hugging Face Embeddings
* Groq LLM
* Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```text
AI-Lawyer-Assistant/
│── app.py
│── main.ipynb
│── requirements.txt
│── .env
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Lawyer-Assistant.git

cd AI-Lawyer-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

PINECONE_API_KEY=your_pinecone_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. Legal documents are converted into embeddings using Hugging Face.
2. The embeddings are stored in Pinecone.
3. A user's legal question is converted into an embedding.
4. Pinecone retrieves the most relevant document chunks.
5. LangChain injects the retrieved context into the prompt.
6. Groq LLM generates an answer using only the retrieved legal documents.
7. The response is displayed through the Streamlit interface.

---

## 📷 Application Preview

Add screenshots of your application here.

Example:

```
images/home.png

images/chat.png
```

---

## 💡 Future Improvements

* PDF upload directly from the UI
* Chat history persistence
* Source citation for retrieved documents
* Multi-document support
* User authentication
* Conversation memory
* Streaming responses
* Dark/Light mode

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Parthiv Baruah**

* GitHub: https://github.com/your-username
* LinkedIn: https://linkedin.com/in/your-profile

---

⭐ If you found this project helpful, consider giving it a star!
