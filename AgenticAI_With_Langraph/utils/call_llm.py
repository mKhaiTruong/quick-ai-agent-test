import os
from dotenv import load_dotenv
load_dotenv()

from langchain_anthropic import ChatAnthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-haiku-4-5-20251001")