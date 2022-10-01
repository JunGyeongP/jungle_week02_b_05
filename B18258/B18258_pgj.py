import sys
from collections import deque


num = int(sys.stdin.readline())
stack_arr = deque([])
for i in range(num):
    command_arr = list(map(str, sys.stdin.readline().strip().split()))
    if(command_arr[0] == 'push'):
        stack_arr.append(int(command_arr[1]))
    elif(command_arr[0] == 'pop'):
        if(len(stack_arr) == 0):
            print(-1)
        else:
            print(f'{stack_arr[0]}')
            stack_arr.popleft()
    elif(command_arr[0] == 'size'):
        print(f'{len(stack_arr)}')
    elif(command_arr[0] == 'empty'):
        if(len(stack_arr) == 0):
            print(1)
        else:
            print(0)
    elif(command_arr[0] == 'back'):
        if(len(stack_arr) == 0):
            print(-1)
        else:
            print(f'{stack_arr[len(stack_arr)-1]}')
        
    elif(command_arr[0] == 'front'):
        if(len(stack_arr) == 0):
            print(-1)
        else:
            print(f'{stack_arr[0]}')