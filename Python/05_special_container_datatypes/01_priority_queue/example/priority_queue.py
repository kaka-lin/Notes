import random

class PriorityQueue(object):
    def __init__(self, idx, img):
        self.idx = idx
        self.img = img

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        return self.idx < other.idx

    def __getitem__(self, key):
        return self.__dict__.get(key)
