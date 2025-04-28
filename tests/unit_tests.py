import unittest
from seedling_core.traits import TraitEngine
from seedling_core.emotions import EmotionAnalyzer

class TestSeedlingModules(unittest.TestCase):
    def test_trait_adjustment(self):
        engine = TraitEngine()
        emotion_context = {"trait_influences": {"curiosity": 0.1}}
        engine.adjust(emotion_context)
        self.assertGreater(engine.get_traits()["curiosity"], 0.5)

    def test_emotion_analyze(self):
        analyzer = EmotionAnalyzer()
        result = analyzer.analyze("I feel sad and lonely")
        self.assertEqual(result["emotion"], "sadness")

if __name__ == '__main__':
    unittest.main()
