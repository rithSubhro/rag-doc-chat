import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI Assistant")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3")

settings = Settings()
