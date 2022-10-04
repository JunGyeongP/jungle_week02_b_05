import sys
from collections import deque

def turn(alpha):
    global direction
    if(alpha == 'L'):
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4


N = int(sys.stdin.readline())
# 맵 크기
K = int(sys.stdin.readline())
# 사과 수


graph = [[0] * N for _ in range(N)]
# 맵 생성

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2
    # 사과를 좌표에 배치

L = int(sys.stdin.readline())
dirDict = dict()
queue = deque()
queue.append((0,0))

for i in range(L):
    x, c = input().split()
    dirDict[int(x)] = c

x,y = 0 , 0 #최초 좌표 설정
graph[x][y] = 1 #뱀 위치 선정
cnt = 0
direction = 0

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if(x< 0 or x >= N or y < 0 or y >= N):
        break

    if(graph[x][y] == 2):
        graph[x][y] = 1
        queue.append((x,y))
        if(cnt in dirDict):
            turn(dirDict[cnt])

    elif(graph[x][y] == 0):
        graph[x][y] = 1
        queue.append((x,y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if (cnt in dirDict):
            turn(dirDict[cnt])

    else:
        break

print(cnt)

