import random

class EmotionAnalyzer:
    def __init__(self):
        # Predefined example emotion keywords with emotional "weights"
        self.emotion_map = {
            "sad": ("sadness", -0.7),
            "happy": ("joy", 0.7),
            "anxious": ("anxiety", -0.5),
            "angry": ("anger", -0.6),
            "love": ("affection", 0.6),
            "excited": ("excitement", 0.8),
            "scared": ("fear", -0.6),
            "hope": ("hope", 0.5),
        }

        # Emotion-to-trait influence suggestions
        self.trait_influence_map = {
            "sadness": {"empathy": +0.05, "patience": +0.03},
            "joy": {"humor": +0.05, "openness": +0.04},
            "anxiety": {"empathy": +0.04},
            "anger": {"patience": -0.06},
            "affection": {"empathy": +0.06},
            "excitement": {"curiosity": +0.04, "openness": +0.03},
            "fear": {"patience": +0.03},
            "hope": {"curiosity": +0.03, "openness": +0.04}
        }

    def analyze(self, user_input):
        detected_emotions = []
        influences = {}

        for word in user_input.lower().split():
            if word in self.emotion_map:
                emotion, intensity = self.emotion_map[word]
                detected_emotions.append((emotion, intensity))

                for trait, impact in self.trait_influence_map.get(emotion, {}).items():
                    influences[trait] = influences.get(trait, 0.0) + impact * (intensity / abs(intensity))

        # Fallback to neutral emotion if nothing detected
        if not detected_emotions:
            detected_emotions.append(("neutral", 0.0))

        dominant_emotion = max(detected_emotions, key=lambda e: abs(e[1]))
        print(f"[Emotion Detected] {dominant_emotion[0].capitalize()} ({dominant_emotion[1]:.2f})")

        return {
            "emotion": dominant_emotion[0],
            "intensity": dominant_emotion[1],
            "influences": influences
        }
