
import random

class IntentGenerator:
    def __init__(self, trait_engine, emotion_analyzer, memory_manager):
        self.traits = trait_engine
        self.emotions = emotion_analyzer
        self.memory = memory_manager

    def generate(self, user_input, emotion_context):
        dominant_emotion = max(emotion_context, key=lambda k: float(emotion_context[k]))
        intensity = emotion_context[dominant_emotion]
        tone = self._map_emotion_to_tone(dominant_emotion, intensity)

        # Use emotion and trait influence to craft a dynamic response
        response = self._generate_dynamic_reply(user_input, dominant_emotion, intensity)

        return {
            "tone": tone,
            "response": response
        }

    def _map_emotion_to_tone(self, emotion, intensity):
        tone_map = {
            "joy": "warm",
            "sadness": "gentle",
            "anger": "firm",
            "fear": "calm",
            "surprise": "thoughtful",
            "neutral": "neutral"
        }
        return tone_map.get(emotion, "neutral")

    def _generate_dynamic_reply(self, user_input, emotion, intensity):
        templates = {
            "joy": [
                "That's wonderful to hear!",
                "I'm glad you shared that with me.",
                "It makes me happy to know that."
            ],
            "sadness": [
                "I'm here for you.",
                "That sounds really difficult. Do you want to talk more about it?",
                "I appreciate you opening up about that."
            ],
            "anger": [
                "That seems frustrating. Want to unpack it together?",
                "You have every right to feel upset.",
                "Let's try to find a way forward from this."
            ],
            "fear": [
                "You're not alone in feeling that way.",
                "Would it help to talk about what's making you anxious?",
                "I can stay with you through it."
            ],
            "surprise": [
                "Wow, that's unexpected!",
                "That must have caught you off guard.",
                "What do you think it means?"
            ],
            "neutral": [
                "I'm listening.",
                "Go on, I'm here.",
                "Tell me more."
            ]
        }

        reply_options = templates.get(emotion, templates["neutral"])
        chosen_reply = random.choice(reply_options)
        return f"{chosen_reply} You said: \"{user_input}\""