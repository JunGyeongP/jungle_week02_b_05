import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
liq_list = list(map(int, input().split()))
liq_list.sort()  # 리스트를 순서대로 정렬

picked_liq = list(combinations(liq_list, 2))  # 요소가 2개인 조합 완성.

less0_max = - sys.maxsize
more0_min = sys.maxsize
# 최댓값 최솟값 변수 할당

for liq in picked_liq:
    if sum(liq) == 0:
        print(liq)
    # 두 변수의 합이 0이면 바로 출력
    elif sum(liq) > 0:
        if sum(liq) < more0_min:
            more0_min = sum(liq)
            more_ans = liq
    # 음수
    else:
        if sum(liq) > less0_max:
            less0_max = sum(liq)
            less_ans = liq
    # 양수

if (0-less0_max) < (0+more0_min):
    print(less_ans)
else:
    print(more_ans)
