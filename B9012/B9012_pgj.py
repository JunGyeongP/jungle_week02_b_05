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
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행
        if (len(stack) == 0): #스택에 짝 없는 (이 없을 경우
            print("YES")
        else: # 스택에 (가 남아있는 경우
            print("NO")