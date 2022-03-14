import unittest

from lowercase import lowercase


class LowerCaseTestCase(unittest.TestCase):

    def test_empty_str(self):
        res = lowercase("")
        for r in res:
            self.assertEqual(r, "")
            

    def test_mixed_cases(self):
        tokens = ["heLLo", "WoRlD"]
        expectedRes = ["hello", "world"]
        res= lowercase(tokens)
        i = 0
        for r in res:
            self.assertEqual(r, expectedRes[i])
            i = i+1


if __name__ == '__main__':
    unittest.main()