"""Simulate Deque."""


class Deque:
    """Simulate Deque."""

    def __init__(self, n):
        """Initialize Deque."""
        self.queue = [None] * n
        self.left = n-1
        self.right = 0

    def append(self, x):
        """Append an element to the right."""
        self.queue[self.right] = x
        self.right = (self.right + 1) % len(self.queue)

    def appendleft(self, x):
        """Append an element to the left."""
        self.queue[self.left] = x
        self.left = (self.left - 1) % len(self.queue)

    def pop(self):
        """Pop an element from the left."""
        value = self.queue[self.right-1]
        self.queue[self.right-1] = None
        self.right = (self.right - 1) % len(self.queue)
        return value

    def popleft(self):
        """Pop an element from the right."""
        value = self.queue[(self.left+1) % len(self.queue)]
        self.queue[(self.left+1) % len(self.queue)] = None
        self.left = (self.left + 1) % len(self.queue)
        return value

    def peek(self):
        """Peek an element to the right."""
        return self.queue[(self.right-1) % len(self.queue)]

    def peekleft(self):
        """Peek an element to the left."""
        return self.queue[(self.left+1) % len(self.queue)]

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
        value = self.queue[(self.right) % len(self.queue)]
        if self.right == self.left + len(self.queue) + 1:
            raise StopIteration
        else:
            self.right = self.right + 1
            return value
