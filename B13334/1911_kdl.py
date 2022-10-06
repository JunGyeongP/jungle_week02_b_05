import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    line = tuple(map(int, input().split()))
    lines.append(line)
    # 리스트보다 튜플이 저장속도 및 인덱싱 속도가 더 빠르다
lines.sort()

l = lines[0][0]
r = lines[0][1]
res = 0

for i in range(1, len(lines)):
    if lines[i][0] <= r < lines[i][1]:
        r = lines[i][1]
    elif r < lines[i][0]:
        res += r - l
        l = lines[i][0]
        r = lines[i][1]

res += r - l

print(res)
