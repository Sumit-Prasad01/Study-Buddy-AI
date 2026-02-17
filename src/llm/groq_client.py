from langchain_groq import ChatGroq
from src.config.settings import settings


def get_groq_llm():
    
    return ChatGroq(
        api_key = settings.GROQ_API_KEY,
        temperature = settings.TEMPERATURE,
        max_retries = settings.MAX_RETRIES
    )