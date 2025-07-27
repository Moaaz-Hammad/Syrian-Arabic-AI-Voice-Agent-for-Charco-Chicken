import whisper

def transcribe(audio_path, language='ar'):
    model = whisper.load_model('base')
    result = model.transcribe(audio_path, language=language)
    return result['text'] 