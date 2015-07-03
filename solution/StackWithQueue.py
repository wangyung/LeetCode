from collections import deque

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        oldCount = len(self.queue)
        self.queue.append(x)
        for i in range(0, oldCount, 1):
            self.queue.append(self.queue.popleft())

    # @return nothing
    def pop(self):
        if not self.empty():
            self.queue.popleft()

    # @return an integer
    def top(self):
        if not self.empty():
            return self.queue[0]
        else:
            return None

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0

def test1():
    print "test1: "
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)

    while not stack.empty():
        print stack.top()
        stack.pop()

def test2():
    print "test2"
    stack = Stack()
    stack.push(1)
    stack.pop()
    stack.push(2)
    stack.push(5)
    stack.pop()
    stack.pop()
    stack.push(100)
    stack.push(101)
    stack.pop()
    stack.pop()
    stack.pop()

    while not stack.empty():
        print stack.top()
        stack.pop()

if __name__ == "__main__":
    test1()
    test2()