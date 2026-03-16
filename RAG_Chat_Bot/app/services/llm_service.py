from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

def get_llm():
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )
