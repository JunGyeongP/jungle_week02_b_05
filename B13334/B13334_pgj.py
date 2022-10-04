import sys
import heapq

n = int(sys.stdin.readline())

list = []
heap = []
maxi = 0
for i in range(n):
    h, a = map(int, sys.stdin.readline().strip().split())
    if h > a:
        list.append((a,h))
    else:
        list.append((h,a))
d = int(sys.stdin.readline())
list.sort(key=lambda x: (x[1], x[0]))

for i in range(len(list)):
    rp = list[i][1]
    lp = list[i][0]

    if rp-lp <= d:
        heapq.heappush(heap, lp)

    else:
        continue

    while len(heap) != 0:
        tmp = heap[0]
        if rp-tmp <= d:
            break
        else:
            heapq.heappop(heap)

    maxi = max(maxi, len(heap))

print(maxi)
