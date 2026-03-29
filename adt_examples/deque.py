

class Deque:

    def __init__(self, n):
        self.queue = [None] * n
        self.left = 0
        self.right = n-1

    def append(self, x):
        self.queue[self.right] = x
        self.right = (self.right - 1) % len(self.queue)

    def appendleft(self, x):
        self.queue[self.left] = x
        self.left = (self.left + 1) % len(self.queue)

    def popleft(self):
        value = self.queue[self.right]
        self.queue[self.right] = None
        self.right = (self.right + 1) % len(self.queue)
        return value

    def pop(self):
        value = self.queue[self.left]
        self.queue[self.left] = None
        self.left = (self.left - 1) % len(self.queue)
        return value

    def peek(self):
        return self.queue[(self.right+1) % len(self.queue)]

    def peekleft(self):
        return self.queue[(self.left-1) % len(self.queue)]

    def __len__(self):
        length = 0
        for i in range(len(self.queue)):
            if self.queue[i] is not None:
                length += 1
        return length

    def __iter__(self):
        return DequeIterator(self)


class DequeIterator:

    def __init__(self, deque):
        self.queue = deque.queue
        self.left = deque.left
        self.right = deque.right

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self.queue)
        index = 0
        if index < length:
            value = self.queue[index]
            index += 1
        else:
            raise StopIteration
        return value
