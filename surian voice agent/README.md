# Syrian Arabic Voice Agent

## Overview
A prototype voice agent for Charco Chicken that handles real-time SIP calls, transcribes and understands Syrian Arabic, and processes orders with a Streamlit UI for testing.

## Features
- Real-time SIP call handling (LiveKit)
- Whisper for STT (Speech-to-Text)
- ElevenLabs for TTS (Text-to-Speech)
- Intent detection and order processing
- Streamlit UI for testing and demo

## Setup

### Prerequisites
- Python 3.9+
- ffmpeg installed
- Accounts/API keys for LiveKit, ElevenLabs

### Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the root directory:
```
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=wss://your-livekit-server
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=your_syrian_arabic_voice_id
```

## Running the Project

### 1. Start the backend API
```bash
uvicorn backend:app --reload
```

### 2. Start the SIP Agent
```bash
python sip_agent.py
```

### 3. Start the Streamlit UI
```bash
streamlit run app.py
```

## SIP Configuration
- Configure your SIP trunk with LiveKit or your provider.
- Update credentials in `.env`.

## Testing
- Use the Streamlit UI to upload audio or type Arabic.
- Call the SIP number to interact with the agent in real time. 