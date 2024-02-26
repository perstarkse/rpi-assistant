import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

def text_to_speech(message: str, id: str) -> str:
  """
  Converts text to speech using the ElevenLabs API.

  Args:
    message (str): The text to convert to speech.
    id (str): The id of the audio file.

  Returns:
    str: The filepath of the saved audio file.
  """

  CHUNK_SIZE = 1024
  url = "https://api.elevenlabs.io/v1/text-to-speech/TiWWRZSd9ZOnzOuNXUa0"

  headers = {
    "Accept": "audio/wav",
    "Content-Type": "application/json",
    "xi-api-key": api_key
  }

  data = {
    "text": message,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)

  filepath = f"outputs/{id}.mp3"

  with open(filepath, 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
      if chunk:
        f.write(chunk)

  print(f"Audio file saved to {filepath}")
  return filepath
