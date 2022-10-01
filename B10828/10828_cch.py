class Stack:
    def __init__(self, N):
        self.stack = [None] * N
        self.now = -1

    def push(self, e):
        self.now += 1
        self.stack[self.now] = e

    def pop(self):
        if self.now == -1:
            print("-1")
        else:
            e = self.stack[self.now]
            self.now -= 1
            print(e)

    def size(self):
        print(self.now + 1)

    def empty(self):
        if self.now == -1:
            print("1")
        else:
            print("0")

    def top(self):
        if self.now == -1:
            print("-1")
        else:
            print(self.stack[self.now])

    def custom_function(self, arr):
        command = arr[0]
        if command == 'push':
            self.push(arr[1])
        elif command == 'pop':
            self.pop()
        elif command == 'size':
            self.size()
        elif command == 'empty':
            self.empty()
        elif command == 'top':
            self.top()

import sys
N = int(sys.stdin.readline())
stack = Stack(N)
for _ in range(N):
    li = list(sys.stdin.readline().split())
    stack.custom_function(li)  
