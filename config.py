import os
import sys

# Load from .env file in development, but Render uses environment variables directly
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
DATABASE_PATH = "conversations.db"
PORT = int(os.environ.get("PORT", 5000))

# Debug logging
if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY not set!", file=sys.stderr)
    print(f"Available env vars: {list(os.environ.keys())}", file=sys.stderr)




