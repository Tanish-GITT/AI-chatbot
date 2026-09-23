from openai import OpenAI
from config import OPENAI_API_KEY
from memory import Memory
import os

class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.memory = Memory()
        self.model = "gpt-4o-mini"

        # Load knowledge base
        self.knowledge_base = self.load_knowledge_base()

        self.system_prompt = f"""You are a helpful AI assistant representing Tanish Saini, an AI and backend developer.

Here's information about Tanish:

{self.knowledge_base}

When users ask about Tanish, his projects, skills, or experience, use this information to provide accurate, personalized responses.
Be friendly and professional. If asked something not in the knowledge base, be honest that you don't have that information.
Always encourage them to visit the portfolio or reach out via the provided contact information."""

    def load_knowledge_base(self):
        """Load knowledge base from file"""
        kb_path = "knowledge_base.txt"
        if os.path.exists(kb_path):
            try:
                with open(kb_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                print(f"Error loading knowledge base: {e}")
                return "Information about Tanish is currently unavailable."
        return "Information about Tanish is currently unavailable."

    def chat(self, conversation_id, user_message):
        # Get conversation history
        history = self.memory.get_conversation_history(conversation_id)

        # Build messages for API
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        # Get response from OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )

        assistant_message = response.choices[0].message.content

        # Save to memory
        self.memory.add_message(conversation_id, "user", user_message)
        self.memory.add_message(conversation_id, "assistant", assistant_message)

        return assistant_message

