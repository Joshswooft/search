from collections import defaultdict
import unittest
from indexer.index import SearchHits, create_dict

from models.product import Product
from search import format_results, transform_search_hits_to_search_results
from models.search_result import SearchResult


class SearchTestCase(unittest.TestCase):
    
    def test_format_results_empty(self):
        expected = []
        self.assertEqual(expected, format_results([]))

    def test_format_results(self):
        expected = [
            {'Score': 1.2, 'product': {'brand': 'nike', 'id': 1, 'name': 'shoe'}},
            {'Score': 0.8, 'product': {'brand': 'assos', 'id': 2, 'name': 'hat'}}
        ]
        res = [SearchResult(1.2, Product(1,"shoe","nike")), SearchResult(0.8, Product(2, "hat", "assos"))]
        actual = format_results(res)
        self.assertEqual(expected, actual)

    def test_transform_search_hits(self):
        hits = [SearchHits(1, 0.7)]
        p = Product(1, "hi", "nike")
        docs = defaultdict(create_dict)
        docs[1] = { "id": 1, "name": "hi", "brand": "nike" }

        expected = [SearchResult(0.7, p)]
        actual = transform_search_hits_to_search_results(hits, docs)
        self.assertEqual(expected, actual)

    def test_transform_search_hits_to_search_results_empty(self):
        docs = [{ "id": 2, "name": "Stripe T shirt", "brand": "Prada" }]
        hits = []
        expected = []
        actual = transform_search_hits_to_search_results(hits, docs)
        self.assertEqual(expected, actual)
    


if __name__ == '__main__':
    unittest.main()