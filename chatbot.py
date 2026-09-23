from openai import OpenAI
from config import OPENAI_API_KEY
from memory import Memory

class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.memory = Memory()
        self.model = "gpt-4o-mini"
        self.system_prompt = """You are a helpful and friendly assistant.
Provide clear, concise, and accurate responses.
If you don't know something, be honest about it."""

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
