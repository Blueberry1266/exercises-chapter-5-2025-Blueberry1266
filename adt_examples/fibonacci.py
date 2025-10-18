"""Form Fibonacci sequence."""


class Fib:
    """It's an infinite Fibonacci sequence."""

    def __init__(self):
        """Initialize the first link."""
        self.current = 1
        self.following = 1

    def __iter__(self):
        """Iterator."""
        return self

    def __next__(self):
        """Define the next link."""
        self.current, self.following = (
            self.following, self.current + self.following
        )
        return self.current
