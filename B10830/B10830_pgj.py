import sys
def mul(U, V):
    N = len(U)
    Z = [[0]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            sum = 0
            for i in range(N):
                sum += U[r][i] * V[i][c]
            Z[r][c] = sum % 1000

    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)


N, B = map(int, sys.stdin.readline().split())
A = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]

result = square(A, B)

for r in result:
    print(*r)