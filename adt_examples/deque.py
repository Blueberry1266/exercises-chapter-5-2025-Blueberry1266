

class Deque:

    def __init__(self, length):
        self.deque = [None]*length
        self.left = 0
        self.right = length - 1

    def append(self, x):
        self.deque[self.right] = x
        self.right = (self.right-1) % len(self.deque)
        return self.deque

    def appendleft(self, x):
        self.deque[self.left] = x
        self.left = (self.left+1) % len(self.deque)
        return self.deque

    def pop(self):
        val = self.deque[(self.right+1) % len(self.deque)]
        self.right = (self.right + 1) % len(self.deque)
        self.deque[self.right] = None
        return val

    def popleft(self):
        val = self.deque[(self.left-1) % len(self.deque)]
        self.left = (self.left - 1) % len(self.deque)
        self.deque[self.left] = None
        return val

    def peek(self):
        return self.deque[(self.right+1) % len(self.deque)]

    def peekleft(self):
        return self.deque[(self.left-1) % len(self.deque)]

    def __len__(self):
        length = 0
        for i in range(len(self.deque)):
            if self.deque[i] is not None:
                length += 1
        return length

    def __iter__(self):
        return DequeIterator(self.deque, self.left)


class DequeIterator:
    def __init__(self, deque, left):
        self.deque = deque
        self.left = left
        self.index = 1

    def __len__(self):
        length = 0
        for i in range(len(self.deque)):
            if self.deque[i] is not None:
                length += 1
        return length

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= len(self):
            self.index += 1
            self.left -= 1
            return self.deque[self.left]
        else:
            raise StopIteration
