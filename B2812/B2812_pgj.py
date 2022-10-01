import sys

N,K = map(int, sys.stdin.readline().strip().split())
num = list(input())

k = K
stack = []
for i in range(N):
    while k >0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])



print(''.join(stack[:N-K]))