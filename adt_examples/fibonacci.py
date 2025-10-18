

class Fib:

    def __init__(self):
        self.current = 1
        self.following = 1

    def __iter__(self):
        return FibIterator(self)


class FibIterator:

    def __init__(self, fibn):
        self.here = fibn

    def __iter__(self):
        return self

    def __next__(self):
        value = self.here.current
        self.here.current, self.here.following = self.here.following, value
        + self.here.following
        return value


"""
class Fib:
    def __iter__(self):
        # 每次 for 循环都会生成一个独立的迭代器
        return FibIterator()


class FibIterator:
    def __init__(self):
        self.current = 1
        self.following = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current, self.following = self.following, value + self.following
        return value
"""
