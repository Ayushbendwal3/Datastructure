from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == "__main__":
    a = Queue()
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in num_list:
        a.enqueue(bin(i)[2:])

    for i in range(a.size()):
        print(a.dequeue())
