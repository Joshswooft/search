import unittest

from text_analyzer import TextAnalyzer
from token_filters.lowercase import lowercase
from token_filters.remove_punctuation import remove_punctuation


class TextAnalyzerTestCase(unittest.TestCase):
    def test_parse(self):
        analyzer = TextAnalyzer()
        analyzer.token_filters = [remove_punctuation, lowercase]
        text = "INSIDE VOICE please!!!"
        expected = ["inside", "voice", "please"]
        expected.sort()
        tokens = list(analyzer.parse(text))
        tokens.sort()
        self.assertEqual(expected, tokens)

if __name__ == '__main__':
    unittest.main()