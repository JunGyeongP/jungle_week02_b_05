import sys
from collections import deque

num = int(sys.stdin.readline())

num_arr = deque([])
for i in range(num):
    num_arr.append(i+1)


while (len(num_arr) > 1):
    num_arr.popleft()
    num_arr.append(num_arr[0])
    num_arr.popleft()

print(num_arr[0])