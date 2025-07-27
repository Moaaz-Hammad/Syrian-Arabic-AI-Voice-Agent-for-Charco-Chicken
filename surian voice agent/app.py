import streamlit as st
import requests
import os
from stt import transcribe
from tts import synthesize
from intent import detect_intent

BACKEND_URL = 'http://localhost:8000/submit-order'

def main():
    st.title('Syrian Arabic Voice Agent Demo')
    st.write('Upload an audio file or type Arabic text to interact with the agent.')

    input_mode = st.radio('Input mode:', ['Audio', 'Text'])
    user_text = ''
    audio_path = None

    if input_mode == 'Audio':
        audio_file = st.file_uploader('Upload audio (wav/mp3)', type=['wav', 'mp3'])
        if audio_file is not None:
            audio_path = f'temp_{audio_file.name}'
            with open(audio_path, 'wb') as f:
                f.write(audio_file.read())
            user_text = transcribe(audio_path)
            st.write('**Transcribed Text:**', user_text)
    else:
        user_text = st.text_area('اكتب بالعربية هنا')

    if user_text:
        intent = detect_intent(user_text)
        st.write('**Detected Intent:**', intent)
        agent_response = ''
        if intent == 'order':
            name = st.text_input('اسم الزبون')
            order_list = st.text_area('قائمة الطلبات (افصل كل عنصر بسطر)')
            if st.button('Submit Order'):
                order_items = [item.strip() for item in order_list.split('\n') if item.strip()]
                resp = requests.post(BACKEND_URL, json={'name': name, 'order': order_items})
                if resp.ok:
                    data = resp.json()
                    agent_response = f"تم استلام طلبك! رقم الطلب: {data['order_id']}, الوقت المتوقع: {data['eta']}"
                else:
                    agent_response = 'حدث خطأ أثناء إرسال الطلب.'
        elif intent == 'complaint':
            agent_response = 'نعتذر عن أي إزعاج. سنقوم بمساعدتك فوراً.'
        elif intent == 'question':
            agent_response = 'سعيدون بالإجابة على أسئلتك!'
        else:
            agent_response = 'لم أفهم طلبك. هل يمكنك التوضيح؟'
        st.write('**Agent Response:**', agent_response)
        if agent_response:
            audio_out = synthesize(agent_response)
            st.audio(audio_out, format='audio/wav')

if __name__ == '__main__':
    main() 