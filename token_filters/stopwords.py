from pathlib import Path

def stopword_getter(path=Path(__file__).parent / "../stop_words_english.txt"):
    with path.open() as file:
        return file.read().splitlines()


def remove_stopwords(tokens, stopword_getter=stopword_getter):
    stopwords = stopword_getter()
    for token in tokens:
        if token not in stopwords:
            yield token
