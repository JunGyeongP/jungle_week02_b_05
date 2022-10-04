import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(input())
stk = []

for i in range(len(numbers)):
    n = len(stk)
    while K > 0 and stk:
        if stk[-1] < numbers[i]:
            stk.pop()
            K -= 1
        elif stk[-1] >= numbers[i]:
            break
    stk.append(numbers[i])

print(''.join(stk))
