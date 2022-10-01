import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

stk = []
cnt = 0

for i in range(N):
    stk.append(int(input()))

r = stk.pop()
cnt += 1

for _ in range(len(stk)):
    x = stk.pop()
    if x > r:
        r = x
        cnt += 1

print(cnt)
