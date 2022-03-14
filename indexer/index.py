from collections import defaultdict, Counter
from dataclasses import dataclass
import json
from indexer.pickle import PickleReader, PickleWriter
from text_analyzer import TextAnalyzer

def create_dict():
    return defaultdict(Counter)

@dataclass
class SearchHits():
    docId: str
    score: float

@dataclass
class InvertedIndex:
    analyzer = TextAnalyzer()
    index = defaultdict(create_dict)
    writer = PickleWriter
    reader = PickleReader
    
    # creates the initial index as a Dictionary of "term" -> { docId: count }
    # count = number of times it appears in doc
    def create_from_files(self, files):
        for f in files:
            doc = json.load(f)
            self.index_document(doc)
        self.writer.save(self.index)

    def index_documents(self, docs):
        for doc in docs:
            self.index_document(doc)
        self.writer.save(self.index)

    def index_document(self, doc):
        id = doc["id"]
        for field in doc:
            if isinstance(doc[field], str):
                for token in self.analyzer.parse(doc[field]):
                    self.index[field][token][id] += 1

    def load(self, filename: str):
        self.index = self.reader.load(filename)
        return self.index

    def search(self, term:str, limit=10)->list[SearchHits]:
        fields = self.index.keys()

        # if we have 100,000 matches here this could blow up
        out = list()
        for token in self.analyzer.parse(term):
            for field in fields:
                doc = self.index[field][token]
                if not doc:
                    continue
                out.append(doc)
                

        # we add 1 point each time the docId was found in the index
        scores = Counter()
        for c in out:
            for docId in c:
                scores[docId] += 1
        
        results = []
        for docId, score in scores.most_common(limit):
            results.append(SearchHits(docId, float(score)))
        return results

