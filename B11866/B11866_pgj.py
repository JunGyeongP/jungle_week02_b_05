import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
num_list = deque([])
for i in range(N):
    num_list.append(i+1)
print(num_list)
result_arr = []
while(len(result_arr) < N):
    cnt = 1
    while(cnt < K):
        num_list.append(num_list[0])
        num_list.popleft()
        cnt += 1
    result_arr.append(num_list[0])
    num_list.popleft()
print("<",end="")
for i in range(len(result_arr)):
    print(result_arr[i], end="")
    if(i != len(result_arr)-1):
        print(",", end=" ")
print(">")