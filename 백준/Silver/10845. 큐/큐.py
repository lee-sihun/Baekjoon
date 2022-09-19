import sys 


class Que:
    def __init__(self):
        self.que = []

    def push(self, x):
        self.que.append(x)

    def pop(self):
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
que = Que()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.push(command[1])
    elif command[0] == 'pop':
        print(que.pop())
    elif command[0] == 'size':
        print(que.size())
    elif command[0] == 'empty':
        print(que.empty())
    elif command[0] == 'front':
        print(que.front())
    elif command[0] == 'back':
        print(que.back())