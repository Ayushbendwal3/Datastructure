# reversing array using stack
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def top(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    stack = Stack()
    string = "My name is Ayush"
    for i in string:
        stack.push(i)

    for i in range(stack.size()):
        print(stack.pop(), end="")
