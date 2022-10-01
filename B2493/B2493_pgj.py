import sys

num = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().strip().split()))
stack = []
answer = []
for i in range(num):
    while stack:
        if(stack[-1][1] > top[i]):
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if(not stack):
        answer.append(0)
    stack.append([i,top[i]])


for i in range(num):
     print(answer[i],end=" ")
