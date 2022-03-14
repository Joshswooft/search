# ideally use porter stemmer or similar - just for show
def stem(tokens):
    for token in tokens:
        if token.endswith('ly'):
            token = token[:-2]
        yield token