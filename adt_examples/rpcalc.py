from numpy import sin, cos


class RPCalc:

    def __init__(self):
        self.stack = []

    def pop(self):
        pop_item = self.stack.pop()
        return pop_item

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def push(self, n):
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
        
