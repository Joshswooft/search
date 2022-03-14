from collections import defaultdict
import pickle

class PickleWriter():
    def save(index: defaultdict, filename="index.pkl"):
        with open(filename, "wb") as pkl_handle:
            pickle.dump(index, pkl_handle)


class PickleReader():
    def load(filename="index.pkl")->defaultdict:
        with open(filename, "rb") as p:
            return pickle.load(p)