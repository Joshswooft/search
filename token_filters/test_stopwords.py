import unittest

from stopwords import remove_stopwords

class StopWordsTestCase(unittest.TestCase):

    def test_removes_stop_words(self):
        tokens = ["the", "white", "fox", "is", "small"]
        expectedTokens = ["white", "fox", "small"]

        res = remove_stopwords(tokens)

        i = 0
        for token in res:
            self.assertEqual(expectedTokens[i], token)
            i = i + 1
            


if __name__ == '__main__':
    unittest.main()