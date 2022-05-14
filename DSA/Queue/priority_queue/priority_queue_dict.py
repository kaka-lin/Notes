import random

class PriorityQueue(object):
    def __init__(self, idx):
        self.idx = idx

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        return self.idx < other.idx

    def __getitem__(self, key):
        return self.__dict__.get(key)


if __name__ == "__main__":
    output = []
    data = [1, 8, 5, 6, 3, 4, 0, 9, 7, 2]
    for i in data:
        d = PriorityQueue(i)
        output.append(d)

    output.sort()
    print(output)
