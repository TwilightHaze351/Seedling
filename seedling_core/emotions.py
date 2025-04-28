class EmotionAnalyzer:
    def analyze(self, text):
        if any(word in text.lower() for word in ["sad", "upset", "lonely"]):
            return {"emotion": "sadness", "intensity": 0.8, "trait_influences": {"empathy": 0.05}}
        elif "curious" in text.lower():
            return {"emotion": "interest", "intensity": 0.6, "trait_influences": {"curiosity": 0.05}}
        return {"emotion": "neutral", "intensity": 0.1, "trait_influences": {}}
