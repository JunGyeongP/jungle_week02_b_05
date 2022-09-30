import sys

num = int(sys.stdin.readline())

result_arr = []
for i in range(num):
    a = int(sys.stdin.readline())
    if(a == 0):
        result_arr.pop()
    else:
        result_arr.append(a)

print(sum(result_arr))