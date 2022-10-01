import sys


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def empty(self):
        if not self.stack1 and not self.stack2:
            return 1
        else:
            return 0

    def front(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]
        else:
            return -1

    def back(self):
        if self.stack1:
            return self.stack1[-1]
        elif self.stack2:
            return self.stack2[0]
        else:
            return -1


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
order_list = [input().split() for _ in range(N)]

q = Queue()
for order in order_list:
    if 'push' in order:
        q.push(int(order[1]))
    elif 'front' in order:
        print(q.front())
    elif 'back' in order:
        print(q.back())
    elif 'pop' in order:
        print(q.pop())
    elif 'size' in order:
        print(q.size())
    elif 'empty' in order:
        print(q.empty())
