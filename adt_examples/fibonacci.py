"""Form Fibonacci sequence."""


class Fib:
    """It's an infinite Fibonacci sequence."""

    def __init__(self):
        self.current = 1
        self.following = 1

    def __iter__(self):
        """Make it iterator."""
        return self

    def __next__(self):
        """Define what is next."""
        self.current, self.following = (
            self.following, self.current + self.following
        )
        return self.current
