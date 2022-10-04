import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A, B, C = map(int, input().split())


def rec_mult(A, B):
    if B == 1:
        return A
    else:
        if B % 2 == 0:
            n = rec_mult(A, B/2)
            return n * n
        else:
            n = rec_mult(A, (B-1)/2)
            return n * n * n


print(rec_mult(A, B) % C)
