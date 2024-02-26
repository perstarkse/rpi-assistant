import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPGRAM_API_KEY")

def transcribe_audio(buffer):
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "audio/wav"
    }

    # Read the audio file as binary data
    # with open(wav_file_path, "rb") as file:
    #     audio_data = file.read()
    audio_data = buffer

    params = {
        "smart_format": "true",
        "punctuate": "true",
        "language": "sv",
        "model": "nova-2"
    }

    response = requests.post(url, headers=headers, data=audio_data, params=params)

    return response.json()