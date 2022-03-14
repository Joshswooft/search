# Tokenizer splits text into streams of tokens

from dataclasses import dataclass

@dataclass
class Tokenizer():

    splitter = " "
    
    def tokenize(self, field: str):
        yield from set(field.split(self.splitter))
