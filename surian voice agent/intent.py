def detect_intent(text):
    text = text.lower()
    if 'طلب' in text or 'أريد' in text or 'وجبة' in text:
        return 'order'
    elif 'شكوى' in text or 'سيء' in text or 'مشكلة' in text:
        return 'complaint'
    elif 'متى' in text or 'كيف' in text or 'أين' in text or '؟' in text:
        return 'question'
    else:
        return 'fallback' 