import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in Render or .env file.")

FLASK_ENV = os.getenv("FLASK_ENV", "development")
DATABASE_PATH = "conversations.db"
PORT = int(os.getenv("PORT", 5000))

