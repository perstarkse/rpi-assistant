import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

def respond_to_message(message: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You are a helpful assistant. The user is a small child who interacts with you. Adjust all responses accordingly and only answer in swedish.",
            },
            {
            "role": "user",
            "content": message,
            },
        ],
    )
    return completion.choices[0].message.content
