import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
d = int(input())
verified_lines = []

for line in lines:
    l, r = line
    if abs(l-r) <= d:
        line = sorted(line)
        verified_lines.append(line)
verified_lines.sort(key=lambda x: x[1])

possible_people = []
maxV = 0

for v_line in verified_lines:
    if not possible_people:
        heappush(possible_people, v_line)
    else:
        while possible_people[0][0] < v_line[1] - d:
            heappop(possible_people)
            if not possible_people:
                break
        heappush(possible_people, v_line)
    maxV = max(maxV, len(possible_people))

print(maxV)
# for line in lines:
#     start = line[1]
#     end = line[1] - d

#     if abs(line[1] - line[0]) <= d:
#         heappush(possible_people, line)
#     while possible_people[0][0] < end - d:
#         heappop(possible_people)

#     maxV = max(maxV, len(possible_people))

# print(maxV)
