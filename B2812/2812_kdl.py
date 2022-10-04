import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(input())
del_num = K
stk = []


for i in range(len(numbers)):
    while del_num > 0 and stk:
        if stk[-1] < numbers[i]:
            stk.pop()
            del_num -= 1
        elif stk[-1] >= numbers[i]:
            break
    stk.append(numbers[i])

print(''.join(stk[:N-K]))
