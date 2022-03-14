# Text Analyzer is comprised of a Tokenizer and zero or more TokenFilters
from dataclasses import dataclass
from token_filters.lowercase import lowercase
from token_filters.remove_punctuation import remove_punctuation
from token_filters.stemmer import stem
from token_filters.stopwords import remove_stopwords
from tokenizer import Tokenizer

@dataclass
class TextAnalyzer():

    tokenizer = Tokenizer()
    token_filters = [lowercase, stem, remove_stopwords, remove_punctuation]

    def parse(self, text: str):
        tokens = self.tokenizer.tokenize(text)
        for token_filter in self.token_filters:
            tokens = token_filter(tokens)

        yield from tokens
