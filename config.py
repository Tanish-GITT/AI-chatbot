import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FLASK_ENV = os.getenv("FLASK_ENV", "development")
DATABASE_PATH = "conversations.db"
PORT = int(os.getenv("PORT", 5000))
