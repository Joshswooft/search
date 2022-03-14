import re

def remove_punctuation(tokens):
    for token in tokens:
        token = re.sub(r'[^\w\s]', '', token)
        yield token