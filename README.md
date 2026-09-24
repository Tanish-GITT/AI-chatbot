# AI Chatbot with Persistent Memory

A simple Python Flask API for an AI chatbot powered by OpenAI, with conversation history stored in SQLite.

## Features

- Chat with an AI assistant
- Persistent conversation history (SQLite database)
- Resume conversations by ID
- Simple REST API
- CORS enabled for frontend integration

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Copy `.env.example` to `.env` and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit `.env`:
```
OPENAI_API_KEY=sk-your-actual-key-here
FLASK_ENV=development
PORT=5000
```

### 3. Run the Server

```bash
python app.py
```

The API will start at `http://localhost:5000`

## API Endpoints

### Create a New Conversation
```http
POST /api/conversation
Content-Type: application/json

{
  "title": "My Chat Session"
}

Response:
{
  "conversation_id": "uuid-here",
  "title": "My Chat Session"
}
```

### Send a Message
```http
POST /api/chat
Content-Type: application/json

{
  "message": "Hello, how are you?",
  "conversation_id": "uuid-here"
}

Response:
{
  "conversation_id": "uuid-here",
  "user_message": "Hello, how are you?",
  "assistant_message": "I'm doing well, thank you for asking!..."
}
```

### Get All Conversations
```http
GET /api/conversations

Response:
{
  "conversations": [
    {
      "id": "uuid-here",
      "title": "My Chat Session",
      "created_at": "2026-09-23T08:00:00",
      "updated_at": "2026-09-23T08:30:00"
    }
  ]
}
```

### Get Specific Conversation
```http
GET /api/conversation/uuid-here

Response:
{
  "id": "uuid-here",
  "title": "My Chat Session",
  "created_at": "2026-09-23T08:00:00",
  "updated_at": "2026-09-23T08:30:00",
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    },
    {
      "role": "assistant",
      "content": "I'm doing well, thank you for asking!..."
    }
  ]
}
```

## Project Structure

```
AI chatbot with persistent memory/
├── app.py              # Flask application
├── chatbot.py          # OpenAI integration
├── memory.py           # SQLite persistence layer
├── config.py           # Configuration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── conversations.db    # SQLite database (auto-created)
└── README.md          # This file
```

## Testing with cURL

```bash
# Create conversation
curl -X POST http://localhost:5000/api/conversation \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Chat"}'

# Send message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi there!", "conversation_id": "YOUR_CONV_ID"}'

# Get all conversations
curl http://localhost:5000/api/conversations
```

## Future Improvements

- PostgreSQL for production
- User authentication
- Rate limiting
- Conversation search
- Export conversations
