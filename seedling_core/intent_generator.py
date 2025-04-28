class IntentGenerator:
    def __init__(self, traits, emotions, memory):
        self.traits = traits
        self.emotions = emotions
        self.memory = memory

    def generate(self, user_input, emotion_context):
        traits = self.traits.get_traits()
        if traits["empathy"] > 0.6:
            tone = "gentle"
        elif traits["curiosity"] > 0.6:
            tone = "inquisitive"
        else:
            tone = "neutral"
        
        response = f"I understand you said: '{user_input}'"
        return {"tone": tone, "response": response}
