import os
from dotenv import load_dotenv

load_dotenv()

# Absolute project root (…/chatbot)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute PDF path (cross-platform safe)
PDF_PATH = os.path.join(BASE_DIR, "data", "Platforms_Supported.pdf")

# LLM config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0))



# PDF path
PDF_PATH = r"C:\Users\HP\OneDrive\Desktop\chatbot\data\Platforms Supported.pdf"
