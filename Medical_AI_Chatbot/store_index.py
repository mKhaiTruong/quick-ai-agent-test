import time
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from src.prompt import system_prompt
from src.call_storage import pinecone
from src.call_llm import llm
from src.helper import *

def slice_and_dice_data(data_path: str = "data/"):
    extracted_data  = load_pdf_files(data=data_path)
    filtered_data   = filter_to_minimal_docs(docs=extracted_data)
    text_chunks     = text_split(minimal_docs=filtered_data)
    return text_chunks

index_name = "medical-chatbot"
if not pinecone.has_index(index_name):
    pinecone.create_index(
        name        = index_name,
        dimension   = 384,
        metric      = 'cosine',
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )
    
    # Wait for index
    while not pinecone.describe_index(index_name).status['ready']:
        time.sleep(1)
        
index = pinecone.Index(index_name)

embedding   = download_hf_embeddings()
text_chunks = slice_and_dice_data(data_path="data/")
docsearch   = PineconeVectorStore.from_documents(
    documents   = text_chunks,
    index_name  = index_name,
    embedding   = embedding, 
)