import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
heap_max_l = []
heap_min_h = []

for number in numbers:
    if not heap_max_l:
        heappush(heap_max_l, -number)
    elif len(heap_max_l) <= len(heap_min_h):
        heappush(heap_max_l, -number)
    else:
        heappush(heap_min_h, number)
    if heap_max_l and heap_min_h:
        if -heap_max_l[0] > heap_min_h[0]:
            l = heappop(heap_min_h)
            r = heappop(heap_max_l)
            heappush(heap_max_l, -l)
            heappush(heap_min_h, -r)
    print(heap_max_l[0]*-1)
