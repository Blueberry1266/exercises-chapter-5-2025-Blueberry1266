

class Deque:
    """A class that implement double end queue."""

    def __init__(self, length):
        """initialize deque."""
        self.deque = [None]*length
        self.left = 0
        self.right = length - 1

    def append(self, x):
        """append an element to the right."""
        self.deque[self.right] = x
        self.right = (self.right-1) % len(self.deque)
        return self.deque

    def appendleft(self, x):
        """append an element to the left."""
        self.deque[self.left] = x
        self.left = (self.left+1) % len(self.deque)
        return self.deque

    def pop(self):
        """leave the right element as None and return."""
        val = self.deque[(self.right+1) % len(self.deque)]
        self.right = (self.right + 1) % len(self.deque)
        self.deque[self.right] = None
        return val

    def popleft(self):
        """leave the left element as None and return."""
        val = self.deque[(self.left-1) % len(self.deque)]
        self.left = (self.left - 1) % len(self.deque)
        self.deque[self.left] = None
        return val

    def peek(self):
        """return the right element."""
        return self.deque[(self.right+1) % len(self.deque)]

    def peekleft(self):
        """return the left element."""
        return self.deque[(self.left-1) % len(self.deque)]

    def __len__(self):
        """retern the length of deque."""
        length = 0
        for i in range(len(self.deque)):
            if self.deque[i] is not None:
                length += 1
        return length

    def __iter__(self):
        """make it iterable."""
        return DequeIterator(self.deque, self.left)


class DequeIterator:
    """iterator for Deque."""
    def __init__(self, deque, left):
        """initialize iterator."""
        self.deque = deque
        self.left = left
        self.index = 1

    def __len__(self):
        """define the length to determine when to stop loop."""
        length = 0
        for i in range(len(self.deque)):
            if self.deque[i] is not None:
                length += 1
        return length

    def __iter__(self):
        """iterator."""
        return self

    def __next__(self):
        """determine what's next."""
        if self.index <= len(self):
            self.index += 1
            self.left -= 1
            return self.deque[self.left]
        else:
            raise StopIteration
