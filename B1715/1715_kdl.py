import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
cards = [int(input())for _ in range(N)]
min_heap = []
sum = 0

for card in cards:
    heappush(min_heap, card)

while len(min_heap) > 1:
    tmp1 = heappop(min_heap)
    tmp2 = heappop(min_heap)
    sum += tmp1+tmp2
    heappush(min_heap, tmp1+tmp2)

print(sum)
