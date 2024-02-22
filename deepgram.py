import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPGRAM_API_KEY")

def transcribe_audio(wav_file_path):
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "url": wav_file_path
    }
    params = {
        "smart_format": "true",
        "punctuate": "true",
        "language": "sv",
        "model": "nova-2"
    }

    response = requests.post(url, headers=headers, json=data, params=params)

    return response.json()
