import os

# Load from .env file in development, but Render uses environment variables directly
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
DATABASE_PATH = "conversations.db"
PORT = int(os.environ.get("PORT", 5000))



