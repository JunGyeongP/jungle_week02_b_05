# 2805 나무 자르기 - 이분 탐색
'''
import sys
N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree_list)

while start <= end:
    mid = (start+end) // 2

    log = 0
    for i in tree_list:
        if i >= mid:
            log += (i - mid)

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
'''
