import sys

num = int(sys.stdin.readline())
num_arr = []

for i in range(num):
    a = int(sys.stdin.readline())
    num_arr.append(a)

max = num_arr[-1]
result = 1
for i in range(len(num_arr)-1, -1, -1):
    if num_arr[i] > max:
        result += 1
        max = num_arr[i]


print(result)