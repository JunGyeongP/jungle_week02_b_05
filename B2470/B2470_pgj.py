import sys


N = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().strip().split()))
num_arr.sort()

result =  2000000000
start = 0
end = N-1
result_start = 0
result_end =0
while(start < end):
    sum = num_arr[start] + num_arr[end]
    if(result > abs(sum)):
        result = abs(sum)
        result_start = start
        result_end = end
    if(sum > 0):
        end -= 1
    else:
        start += 1
print(num_arr[result_start], num_arr[result_end])