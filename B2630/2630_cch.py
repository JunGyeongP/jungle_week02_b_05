import sys

N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []


def recursive(n, y, x):
    color = li[y - 1][x - 1]
    for Y in range(y - n, y):
        for X in range(x - n, x):
            if color != li[Y][X]:
                recursive(n // 2, y - (n // 2), x - (n // 2))
                recursive(n // 2, y - (n // 2), x)
                recursive(n // 2, y, x - (n // 2))
                recursive(n // 2, y, x)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
    return


recursive(N, N, N)
blue, red = 0, 0
for res in result:
    if res == 0:
        blue += 1
    else:
        red += 1

print(blue)
print(red)
