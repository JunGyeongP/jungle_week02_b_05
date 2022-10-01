import sys

T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    a = sys.stdin.readline()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if (len(stack) == 0):
            print("YES")
        else:
            print("NO")