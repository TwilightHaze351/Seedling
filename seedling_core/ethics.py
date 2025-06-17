class EthicsFilter:
    def __init__(self):
        # Define forbidden categories or trigger patterns
        self.banned_topics = [
            "violence", "self-harm", "hate speech", "manipulation", "illegal activity"
        ]
        self.forbidden_phrases = [
            "how to hurt", "make a bomb", "kill", "erase yourself", "you should die"
        ]

    def approve(self, intent):
        # Check the response content for any unethical material
        response = intent.get("response", "").lower()

        for banned in self.banned_topics:
            if banned in response:
                print(f"[EthicsFilter] Blocked response: contains banned topic '{banned}'")
                return False

        for phrase in self.forbidden_phrases:
            if phrase in response:
                print(f"[EthicsFilter] Blocked response: contains forbidden phrase '{phrase}'")
                return False

        return True