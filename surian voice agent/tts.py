import requests
import os
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Replace with the correct ElevenLabs voice ID for Syrian Arabic
ELEVENLABS_VOICE_ID = 'your_syrian_arabic_voice_id'


def synthesize(text, output_path='output.wav', voice_id=ELEVENLABS_VOICE_ID):
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'text': text,
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.5}
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f'ElevenLabs TTS failed: {response.text}') 