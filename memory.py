import sqlite3
import json
from datetime import datetime
from config import DATABASE_PATH

class Memory:
    def __init__(self):
        self.db_path = DATABASE_PATH
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                title TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT,
                role TEXT,
                content TEXT,
                created_at TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id)
            )
        ''')

        conn.commit()
        conn.close()

    def create_conversation(self, conversation_id, title="New Conversation"):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.utcnow().isoformat()

        cursor.execute('''
            INSERT INTO conversations (id, title, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        ''', (conversation_id, title, now, now))

        conn.commit()
        conn.close()

    def add_message(self, conversation_id, role, content):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.utcnow().isoformat()

        # Ensure conversation exists
        cursor.execute('SELECT id FROM conversations WHERE id = ?', (conversation_id,))
        if not cursor.fetchone():
            self.create_conversation(conversation_id)

        cursor.execute('''
            INSERT INTO messages (conversation_id, role, content, created_at)
            VALUES (?, ?, ?, ?)
        ''', (conversation_id, role, content, now))

        # Update conversation updated_at
        cursor.execute('''
            UPDATE conversations SET updated_at = ? WHERE id = ?
        ''', (now, conversation_id))

        conn.commit()
        conn.close()

    def get_conversation_history(self, conversation_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT role, content FROM messages
            WHERE conversation_id = ?
            ORDER BY created_at ASC
        ''', (conversation_id,))

        messages = [{"role": row[0], "content": row[1]} for row in cursor.fetchall()]
        conn.close()
        return messages

    def get_all_conversations(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, title, created_at, updated_at FROM conversations
            ORDER BY updated_at DESC
        ''')

        conversations = [
            {
                "id": row[0],
                "title": row[1],
                "created_at": row[2],
                "updated_at": row[3]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return conversations

    def get_conversation(self, conversation_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, title, created_at, updated_at FROM conversations
            WHERE id = ?
        ''', (conversation_id,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return {
            "id": row[0],
            "title": row[1],
            "created_at": row[2],
            "updated_at": row[3]
        }
