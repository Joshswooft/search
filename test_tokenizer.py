import unittest

from tokenizer import Tokenizer

class TokenizerTestCase(unittest.TestCase):
    
    def test_turns_text_into_tokens(self):
        text = "Be kind"
        expected = ["Be", "kind"]
        tokenizer = Tokenizer()
        tokens = list(tokenizer.tokenize(text))
        tokens.sort()
        i = 0
        for token in tokens:
            self.assertEqual(expected[i], token)
            i = i + 1

    def test_removes_duplicates(self):
        text = "one two three one two four four"
        expected = ["one", "two", "three", "four"]
        expected.sort()
        tokenizer = Tokenizer()
        tokens = list(tokenizer.tokenize(text))
        tokens.sort()
        i = 0
        for token in tokens:
            self.assertEqual(expected[i], token)
            i = i + 1



if __name__ == '__main__':
    unittest.main()