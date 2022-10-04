import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A, B, C = map(int, input().split())


def rec_mult(A, B, C):
    if B == 1:
        return A % C
    else:
        if B % 2 == 0:
            return (rec_mult(A, B/2, C)**2) % C
        else:
            return ((rec_mult(A, (B-1)/2, C)**2)*A) % C


print(rec_mult(A, B, C))
