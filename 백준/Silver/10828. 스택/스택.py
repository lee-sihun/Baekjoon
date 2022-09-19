import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        pop_object = None
        if self.empty() == 1:
            pop_object = -1
        else:
            pop_object = self.items.pop()
        return pop_object

    def size(self):
        return len(self.items)

    def empty(self):
        isEmpty = None
        if len(self.items) == 0:
            isEmpty = 1
        else:
            isEmpty = 0
        return isEmpty

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.items[-1]


n = int(sys.stdin.readline())
stack = Stack()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
