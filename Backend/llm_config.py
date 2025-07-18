import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.language_models import BaseChatModel

load_dotenv()

llm: BaseChatModel = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=512
)
