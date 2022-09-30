import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))


def bin_search(arr, target):
    min_ = 1
    max_ = max(arr)
    while min_ <= max_:
        V_sum = 0
        mid = (min_+max_) // 2
        for i in arr:
            if i > mid:
                V_sum += i - mid
        if V_sum < target:
            max_ = mid - 1
        else:
            min_ = mid + 1
    return max_


print(bin_search(N_list, M))
