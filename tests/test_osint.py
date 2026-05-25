import unittest
import asyncio
from core.engine import AsyncOSINTEngine
from config import SOCIAL_PLATFORMS

class TestOSINTFramework(unittest.TestCase):
    def setUp(self):
        self.engine = AsyncOSINTEngine()
        self.loop = asyncio.get_event_loop()

    def test_config_platforms(self):
        self.assertTrue(len(SOCIAL_PLATFORMS) > 0)
        self.assertIn('github', SOCIAL_PLATFORMS)

    def test_engine_initialization(self):
        self.assertIsNotNone(self.engine.headers)
        self.assertIn('User-Agent', self.engine.headers)

if __name__ == '__main__':
    unittest.main()
