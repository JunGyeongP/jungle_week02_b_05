import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
liq_list = list(map(int, input().split()))
liq_list.sort()

picked_liq = list(combinations(liq_list, 2))

less0_max = - sys.maxsize
more0_min = sys.maxsize

for liq in picked_liq:
    if sum(liq) == 0:
        print(liq)
    elif sum(liq) > 0:
        if sum(liq) < more0_min:
            more0_min = sum(liq)
            more_ans = liq
    else:
        if sum(liq) > less0_max:
            less0_max = sum(liq)
            less_ans = liq

if (0-less0_max) < (0+more0_min):
    print(less_ans)
else:
    print(more_ans)
