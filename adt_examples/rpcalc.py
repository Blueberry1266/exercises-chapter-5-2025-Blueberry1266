"""Reverse Polish Calculator."""

from numbers import Number
import numpy as np


class RPCalc:
    """Reverse Polish Calculator."""

    def __init__(self):
        self.stack = []

    def pop(self):
        """Pop an element."""
        return self.stack.pop()

    def push(self, n):
        """Push an element."""
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "+":
            b = self.pop()
            a = self.pop()
            self.stack.append(a+b)
        elif n == "-":
            b = self.pop()
            a = self.pop()
            self.stack.append(a-b)
        elif n == "*":
            b = self.pop()
            a = self.pop()
            self.stack.append(a*b)
        elif n == "/":
            b = self.pop()
            a = self.pop()
            self.stack.append(a/b)
        elif n == "sin":
            a = self.pop()
            self.stack.append(np.sin(a))
        elif n == "cos":
            a = self.pop()
            self.stack.append(np.cos(a))

    def peek(self):
        """Peek an element."""
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
