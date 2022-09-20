import sys


class Deque:
    def __init__(self):
        self.que = []

    def push_front(self, x):
        self.que.insert(0, x)

    def push_back(self, x):
        self.que.append(x)

    def pop_back(self):
        pop_object = None
        if self.empty() == 1:
            return -1
        else:
            pop_object = self.que.pop()
        return pop_object

    def pop_front(self):
        pop_object = None
        if self.empty() == 1:
            return -1
        else:
            pop_object = self.que[0]
            del self.que[0]
            return pop_object

    def size(self):
        return len(self.que)

    def empty(self):
        if len(self.que) == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.que[0]

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.que[-1]


n = int(sys.stdin.readline())
que = Deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        que.push_front(command[1])
    elif command[0] == 'push_back':
        que.push_back(command[1])
    elif command[0] == 'pop_front':
        print(que.pop_front())
    elif command[0] == 'pop_back':
        print(que.pop_back())
    elif command[0] == 'size':
        print(que.size())
    elif command[0] == 'empty':
        print(que.empty())
    elif command[0] == 'front':
        print(que.front())
    elif command[0] == 'back':
        print(que.back())
