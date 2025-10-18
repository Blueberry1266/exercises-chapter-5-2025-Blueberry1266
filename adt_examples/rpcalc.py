from numpy import sin, cos


class RPCalc:
    """A implementation of Reverse Polish Calculator."""

    def __init__(self):
        """initialize the stack."""
        self.stack = []

    def pop(self):
        """pop the most recent item."""
        pop_item = self.stack.pop()
        return pop_item

    def peek(self):
        """return the most recent item and show the final result."""
        return self.stack[-1]

    def __len__(self):
        """return the length of stack."""
        return len(self.stack)

    def push(self, n):
        """put item in the stack and implement according to the imput."""
        if isinstance(n, int) or isinstance(n, float):
            self.stack.append(n)
        elif n == "+":
            val2 = self.pop()
            val1 = self.pop()
            self.stack.append(val1+val2)
        elif n == "-":
            val2 = self.pop()
            val1 = self.pop()
            self.stack.append(val1-val2)
        elif n == "*":
            val2 = self.pop()
            val1 = self.pop()
            self.stack.append(val1*val2)
        elif n == "/":
            val2 = self.pop()
            val1 = self.pop()
            self.stack.append(val1/val2)
        elif n == "cos":
            val1 = self.pop()
            self.stack.append(cos(val1))
        elif n == "sin":
            val1 = self.pop()
            self.stack.append(sin(val1))
        else:
            raise NotImplementedError
