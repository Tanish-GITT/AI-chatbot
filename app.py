from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from chatbot import Chatbot
from config import PORT, FLASK_ENV
from memory import Memory

app = Flask(__name__)
CORS(app)

memory = Memory()
chatbot = None

def get_chatbot():
    global chatbot
    if chatbot is None:
        chatbot = Chatbot()
    return chatbot

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "OK", "message": "AI Chatbot API is running"})

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' field"}), 400

        user_message = data.get("message")
        conversation_id = data.get("conversation_id", str(uuid.uuid4()))

        # Get response from chatbot
        response = get_chatbot().chat(conversation_id, user_message)

        return jsonify({
            "conversation_id": conversation_id,
            "user_message": user_message,
            "assistant_message": response
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/conversations", methods=["GET"])
def get_conversations():
    try:
        conversations = memory.get_all_conversations()
        return jsonify({"conversations": conversations}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/conversation/<conversation_id>", methods=["GET"])
def get_conversation(conversation_id):
    try:
        conversation = memory.get_conversation(conversation_id)

        if not conversation:
            return jsonify({"error": "Conversation not found"}), 404

        messages = memory.get_conversation_history(conversation_id)
        conversation["messages"] = messages

        return jsonify(conversation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/conversation", methods=["POST"])
def create_conversation():
    try:
        data = request.get_json() or {}
        conversation_id = str(uuid.uuid4())
        title = data.get("title", "New Conversation")

        memory.create_conversation(conversation_id, title)

        return jsonify({
            "conversation_id": conversation_id,
            "title": title
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=(FLASK_ENV == "development"), port=PORT)

