import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
yo_list = deque()
ans = []

for i in range(1, N+1):
    yo_list.append(i)


while yo_list:
    for _ in range(K-1):
        yo_list.append(yo_list.popleft())
    ans.append(yo_list.popleft())


print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print(ans[-1], end='')
print('>')
