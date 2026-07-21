import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from chatbot import get_response


class ChatbotTests(unittest.TestCase):
    def test_greeting_response(self):
        response = get_response("Hello")
        self.assertIn("Hello", response)

    def test_refund_response(self):
        response = get_response("How can I get a refund?")
        self.assertIn("order ID", response)


if __name__ == "__main__":
    unittest.main()
