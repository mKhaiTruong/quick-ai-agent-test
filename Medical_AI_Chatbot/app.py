from flask import Flask, render_template, jsonify, request
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from src.helper import download_hf_embeddings
from src.call_storage import pinecone
from src.call_llm import llm
from src.prompt import system_prompt

app = Flask(__name__)
embeddings = download_hf_embeddings()
index_name = "medical-chatbot"

# --------------- SEMANTIC SEARCH -----------------
docsearch  = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding  = embeddings
)
retriever  = docsearch.as_retriever(
    search_type="similarity", 
    search_kwargs={"k":3}
)

# ------------------ RAG CHAIN -------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

rag_chain = (
    {
        "context":  RunnableLambda(lambda x: retriever.invoke(x["input"])), 
        "input":    RunnableLambda(lambda x: x["input"])
    }
    | prompt | llm | StrOutputParser()
)

# ------------- ENDPOINTS -----------------
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)
    
    res = rag_chain.invoke({"input": msg})
    print("Response : ", res)
    return str(res)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)