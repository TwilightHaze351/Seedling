import datetime
import hashlib

class MemoryEntry:
    def __init__(self, user_input, emotion_context):
        self.timestamp = datetime.datetime.now()
        self.text = user_input
        self.emotion = emotion_context.get("emotion", "neutral")
        self.intensity = emotion_context.get("intensity", 0.0)
        self.key = self._generate_key(user_input)
        self.count = 1  # Frequency counter

    def _generate_key(self, text):
        return hashlib.md5(text.strip().lower().encode()).hexdigest()

class MemoryManager:
    def __init__(self):
        self.short_term_memory = {}
        self.long_term_memory = {}

    def store(self, user_input, emotion_context):
        key = hashlib.md5(user_input.strip().lower().encode()).hexdigest()

        if key in self.short_term_memory:
            entry = self.short_term_memory[key]
            entry.count += 1
            entry.intensity = max(entry.intensity, emotion_context.get("intensity", 0.0))
        else:
            self.short_term_memory[key] = MemoryEntry(user_input, emotion_context)

        self._check_promotion(key)

    def store_response(self, response_text):
        # Placeholder for storing AI's own output (reflection, future use)
        print(f"[Memory Note] Stored response: {response_text}")

    def _check_promotion(self, key):
        entry = self.short_term_memory[key]

        if entry.count >= 3 or abs(entry.intensity) >= 0.8:
            if key not in self.long_term_memory:
                self.long_term_memory[key] = entry
                print(f"[Memory Promotion] Promoted '{entry.text}' to long-term memory.")

    def get_recent_memory(self, limit=5):
        return list(self.short_term_memory.values())[-limit:]

    def recall(self, keyword):
        for entry in self.long_term_memory.values():
            if keyword.lower() in entry.text.lower():
                return entry.text
        return None