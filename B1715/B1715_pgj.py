import sys
import heapq

N = int(sys.stdin.readline())
list = []
for i in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(list, card)

cnt = 0
result = []
while(cnt < N-1):
    card1 = heapq.heappop(list)
    card2 = heapq.heappop(list)
    sum_card = card1 + card2
    heapq.heappush(list, sum_card)
    result.append(sum_card)
    cnt+=1
print(sum(result))
