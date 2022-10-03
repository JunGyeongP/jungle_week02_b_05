import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def multi_matrix(arr1, arr2):
    n = len(arr1)
    AxA = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            ele = 0
            for i in range(n):
                ele += arr1[row][i] * arr2[i][col]
            AxA[row][col] = ele % 1000
    return AxA


def sqr(arr, b):
    if b == 1:
        for row in range(len(arr)):
            for col in range(len(arr)):
                arr[row][col] %= 1000
        return arr

    else:
        if b % 2 == 0:
            tmp = sqr(arr, b//2)
            return multi_matrix(tmp, tmp)
        else:
            tmp = sqr(arr, b-1)
            return multi_matrix(tmp, arr)


for i in sqr(A, B):
    print(*i)
