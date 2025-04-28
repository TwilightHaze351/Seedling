from seedling_core.traits import TraitEngine
from seedling_core.emotions import EmotionAnalyzer
from seedling_core.memory import MemoryManager
from seedling_core.intent_generator import IntentGenerator
from seedling_core.ethics import EthicsFilter

# Initialize subsystems
traits = TraitEngine()
emotions = EmotionAnalyzer()
memory = MemoryManager()
ethics = EthicsFilter()
intent_gen = IntentGenerator(traits, emotions, memory)

def seedling_respond(user_input):
    emotion_context = emotions.analyze(user_input)
    traits.adjust(emotion_context)
    memory.store(user_input, emotion_context)
    
    intent = intent_gen.generate(user_input, emotion_context)
    if not ethics.approve(intent):
        return "I'm not comfortable responding to that."

    # Instead of LLM, simulate output
    response = f"[{intent['tone']} tone] {intent['response']}"
    memory.store_response(response)
    return response

if __name__ == "__main__":
    print("Seedling is online. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        output = seedling_respond(user_input)
        print("Seedling:", output)
