import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
test_cases = [input().split() for _ in range(T)]

for test_case in test_cases:
    stk = []
    isVPS = True
    for j in test_case[0]:
        if j == '(':
            stk.append(j)
        else:
            if len(stk) == 0:
                isVPS = False
                break
            else:
                stk.pop()
        if len(stk) > 0:
            isVPS = False
        else:
            isVPS = True
    if len(stk) == 0 and isVPS == True:
        print('YES')
    else:
        print('NO')
