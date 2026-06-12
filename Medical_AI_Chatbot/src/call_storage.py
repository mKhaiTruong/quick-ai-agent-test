import os
from dotenv import load_dotenv
load_dotenv()

from pinecone import Pinecone 
pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
