from collections import defaultdict
import json
import os
from data_loader import get_docs_from_json_file, get_files, gzip_reader
from indexer.index import InvertedIndex, SearchHits, create_dict
from models.product import Product
from models.search_result import SearchResult
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('term', metavar='term', type=str,
                    help='term to search against')

def format_results(results: list[SearchResult]):
    string_result = []
    for res in results:
        string_result.append(res.to_dict())

    return string_result

def get_product_from_file(file: str)->Product:
    with open(file, 'r') as f:
        p = json.load(f)
        return Product.from_dict(p)

def transform_search_hits_to_search_results(hits: list[SearchHits], docs)->list[SearchResult]:
    res = []
    for hit in hits:
        product = Product.from_dict(docs[hit.docId])
        res.append(SearchResult(hit.score, product))
    return res
    

def main():
    args = parser.parse_args()
    search_term = args.term

    index = InvertedIndex()
    path = os.getcwd() + "/index.pkl"

    file = gzip_reader(file_ending="search_dataset.json.gz")
    docs = get_docs_from_json_file(file)
    forward_index = defaultdict(create_dict)

    print("creating forward index...")
    for doc in docs:
        forward_index[doc["id"]] = doc

    print("created forward index!")
    
    if os.path.isfile(path):
        print("found existing index, attempting to load...")
        index.load(path)
    else:
        print("creating inverted index...")
        index.index_documents(docs)
        print("created inverted index!")

    hits = index.search(search_term)
    res = transform_search_hits_to_search_results(hits, forward_index)
    print(*format_results(res), sep="\n")


if __name__ == '__main__':
    main()