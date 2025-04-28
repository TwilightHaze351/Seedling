class MemoryManager:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store(self, user_input, emotion_context):
        self.short_term.append({"input": user_input, "emotion": emotion_context})

    def store_response(self, response):
        self.short_term.append({"response": response})

    def recall(self):
        return self.long_term[-5:] if self.long_term else []

