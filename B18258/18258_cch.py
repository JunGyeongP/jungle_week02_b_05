import sys
class Queue:
    def __init__(self, capacity):
        self.que = [None] * capacity
        self.no = 0
        self.front = 0
        self.rear = 0

    def push(self, dt):
        self.que[self.rear] = dt
        self.rear += 1
        self.no += 1

    def pop(self):
        if self.no == 0:
            print("-1")
        else:
            print(self.que[self.front])
            self.front += 1
            self.no -= 1

    def size(self):
        print(self.no)

    def empty(self):
        if self.no == 0:
            print("1")
        else:
            print("0")

    def front_function(self):
        if self.no == 0:
            print("-1")
        else:
            print(self.que[self.front])

    def back(self):
        if self.no == 0:
            print("-1")
        else:
            print(self.que[self.rear-1])

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
        elif command == 'front':
            self.front_function()
        elif command == 'back':
            self.back()


N = int(sys.stdin.readline())
que = Queue(N)
for _ in range(N):
    que.custom_function(list(sys.stdin.readline().split()))
