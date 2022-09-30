import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
order_list = [input().rsplit() for _ in range(N)]

stack = []

for order in order_list:
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if stack:
            res = stack.pop()
            print(res)
        else:
            print(-1)
