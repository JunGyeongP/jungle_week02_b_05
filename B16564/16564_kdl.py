import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
each_level = [int(input()) for _ in range(N)]
each_level.sort()

minV = min(each_level)
maxV = max(each_level) + K

while minV <= maxV:
    midV = (minV + maxV) // 2
    tmp = 0
    for i in each_level:
        if i > midV:
            break
        else:
            tmp += midV - i
    if K >= tmp:
        minV = midV + 1
        res = midV
    else:
        maxV = midV - 1

print(res)
