

class Fib:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        return self.first
