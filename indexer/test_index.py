from collections import defaultdict
import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from data_loader import get_files

from indexer.index import InvertedIndex, SearchHits

class DummyWriter():
    def save(index: defaultdict, filename="index.txt"):
        pass

class IndexTestCase(unittest.TestCase):

    def test_search(self):
        index = InvertedIndex()
        index.writer = DummyWriter
        
        files = get_files()

        index.create_from_files(files)

        res = index.search("shirt", 1)
        expectedRes = [SearchHits(docId=1, score=1.0)]
        self.assertEqual(1, len(res))
        self.assertEqual(expectedRes, res)



if __name__ == '__main__':
    unittest.main()