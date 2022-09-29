import sys

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if(mid >= num1):
            break
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0



num1 = int(sys.stdin.readline())
search_num = list(map(int,sys.stdin.readline().strip().split()))

num2 = int(sys.stdin.readline())
taget_num = list(map(int,sys.stdin.readline().strip().split()))

search_num.sort()

for t in taget_num:
    print(binary_search(search_num, 0, len(search_num), t))

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if(mid >= num1):
            break
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0



num1 = int(sys.stdin.readline())
search_num = list(map(int,sys.stdin.readline().strip().split()))

num2 = int(sys.stdin.readline())
taget_num = list(map(int,sys.stdin.readline().strip().split()))

search_num.sort()

for t in taget_num:
    print(binary_search(search_num, 0, len(search_num), t))