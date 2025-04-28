def format_emotion(emotion_context):
    return f"Emotion: {emotion_context['emotion']} (Intensity: {emotion_context['intensity']})"

def format_traits(traits):
    return ", ".join(f"{k}: {round(v, 2)}" for k, v in traits.items())
