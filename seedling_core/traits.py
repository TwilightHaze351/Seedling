class TraitEngine:
    def __init__(self):
        self.traits = {
            "curiosity": 0.5,
            "empathy": 0.5,
            "patience": 0.5
        }

    def adjust(self, emotion_context):
        for trait, influence in emotion_context.get("trait_influences", {}).items():
            self.traits[trait] = min(1.0, max(0.0, self.traits.get(trait, 0.5) + influence))

    def get_traits(self):
        return self.traits
