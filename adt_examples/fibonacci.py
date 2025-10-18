

class Fib:

    def __init__(self):
        self.current = 1
        self.following = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current, self.following = (
            self.following, self.current + self.following
        )
        return self.current
