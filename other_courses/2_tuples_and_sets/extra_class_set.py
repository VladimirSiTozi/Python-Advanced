class Set:
    MIN_SIZE = 10

    def __init__(self, size=10):
        self._size = size
        self.filled = 0
        self.elements = [[] for _ in range(size)]

    def hash_func(self, value):
        return hash(value) % self._size

    def __contains(self, value):
        for i, e in enumerate(self.elements[self.hash_func(value)]):
            if value == e: return 1
        return -1

    def contains(self, value):
        return self.__contains(value) >= 0

    def add(self, value):
        self.elements[self.hash_func(value)].append(value)

    def remove(self, value):
        index = self.__contains(value)
        if index >= 0:
            self.filled -= 1
            self.elements[self.hash_func(value)].pop(index)

    def __str__(self):
        return f'size: {self._size} elements: {self.elements}'

aa = Set()
print(aa.__str__())

