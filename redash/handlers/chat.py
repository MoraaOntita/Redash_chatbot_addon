from flask import request, jsonify
from redash.handlers.base import BaseResource
import os
import requests
from dotenv import load_dotenv


class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            question = value.get("question")

            if not question:
                return jsonify({"error": "Missing 'question' field."}), 400

            # Load env
            load_dotenv()
            groq_api_key = os.getenv("GROQ_API_KEY")

            if not groq_api_key:
                return jsonify({"error": "Missing GROQ_API_KEY in env."}), 500

            # URL of your AI microservice inside Docker network
            CHATBOT_URL = "http://chatbot-service:8000/ask"

            # Send question to chatbot-service
            response = requests.post(
                CHATBOT_URL,
                json={
                    "question": question,
                    "pg_uri": "postgresql+psycopg2://postgres@postgres:5432/postgres",
                    "groq_api_key": groq_api_key
                },
                timeout=300
            )

            result = response.json()
            return jsonify(result)

        except Exception as e:
            return jsonify({"error": str(e)}), 500
