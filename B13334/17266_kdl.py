import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())
P = list(map(int, input().split()))

minV = P[0]
maxV = N

if len(P) == 1:
    minV = max(P[0], N-P[0])

else:
    for i in range(len(P)):
        if i == 0:
            H = P[i]
        elif i == len(P)-1:
            H = N - P[i]
        else:
            D = P[i+1]-P[i]
            if D % 2:
                H = D // 2 + 1
            else:
                H = D // 2
        minV = max(H, minV)

print(minV)
