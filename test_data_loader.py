import json
import unittest
from data_loader import get_docs_from_json_file, gzip_reader


class DataLoaderTestCase(unittest.TestCase):
    
    def test_gzip_load_file(self):
        file = gzip_reader()
        expected_contents = {
            "id": 1,
            "name": "Plaid Shirt",
            "brand": "Prada"
        }
        contents = json.load(next(file))

        self.assertEqual(expected_contents, contents)
    
    def test_load_multiple_json_from_gzip(self):
        file = gzip_reader(file_ending="ex2.json.gz")
        docs = list(get_docs_from_json_file(file))
        
        expected_docs = [
            { "id": 1, "name": "Plaid Shirt", "brand": "Prada" }, 
            { "id": 2, "name": "Stripe T shirt", "brand": "Prada" }
        ]

        self.assertEqual(docs, expected_docs)


if __name__ == '__main__':
    unittest.main()