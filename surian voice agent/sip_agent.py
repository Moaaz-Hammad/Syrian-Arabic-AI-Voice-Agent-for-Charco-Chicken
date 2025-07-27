import os
from dotenv import load_dotenv
# Placeholder imports for LiveKit, STT, TTS
# import livekit
# import whisper
# import elevenlabs

load_dotenv()

LIVEKIT_API_KEY = os.getenv('LIVEKIT_API_KEY')
LIVEKIT_API_SECRET = os.getenv('LIVEKIT_API_SECRET')

# TODO: Implement LiveKit SIP connection and audio streaming
# TODO: Integrate with stt.transcribe and tts.synthesize

def main():
    print('Starting SIP agent...')
    print('LiveKit API Key:', LIVEKIT_API_KEY)
    # Connect to LiveKit, handle SIP calls, stream audio to STT, get TTS response
    pass

if __name__ == '__main__':
    main() 