import unittest

from remove_punctuation import remove_punctuation


class RemovePunctuationTestCase(unittest.TestCase):

    def test_remove_punc(self):
        tokens = ["dear", "john,", "happy", "birthday%", "to", "you!!!"]
        expected = ["dear", "john", "happy", "birthday", "to", "you"]
        res = list(remove_punctuation(tokens))

        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()