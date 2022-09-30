import sys


num = int(sys.stdin.readline())
stack_arr = []
for i in range(num):
    command_arr = list(map(str, sys.stdin.readline().strip().split()))
    if(command_arr[0] == 'push'):
        stack_arr.append(int(command_arr[1]))
    elif(command_arr[0] == 'pop'):
        if(len(stack_arr) == 0):
            print(-1)
        else:
            print(stack_arr[len(stack_arr)-1])
            stack_arr.pop()
    elif(command_arr[0] == 'size'):
        print(len(stack_arr))
    elif(command_arr[0] == 'empty'):
        if(len(stack_arr) == 0):
            print(1)
        else:
            print(0)
    elif(command_arr[0] == 'top'):
        if(len(stack_arr) == 0):
            print(-1)
        else:
            print(stack_arr[len(stack_arr)-1])
        
