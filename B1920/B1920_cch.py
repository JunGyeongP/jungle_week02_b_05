# 1920 수 찾기 - 자료 구조, 이분 탐색
# 탐색시간  list : O(N) / 이분탐색 : O(logN) / Set, Dictonary(in연산) : O(1)
## 이진 탐색 - 탐색시간
'''
import sys

N = int(sys.stdin.readline())
N_list = sorted(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())


def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m - 1)
    else:
        return binary(l, N, m + 1, end)


for l in M_list:
    start = 0
    end = len(N_list) - 1
    print(binary(l, N_list, start, end))
'''
## 집합 자료형
'''
import sys

N = int(sys.stdin.readline())
N_list = sorted(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())


N_set = set(N_list)
for m in M_list:
    if m in N_set:
        print("1")
    else:
        print("0")
'''
