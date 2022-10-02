import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))


def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while start <= end:
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N_list.sort()
for i in M_list:
    print(binary_search(N_list, i))
