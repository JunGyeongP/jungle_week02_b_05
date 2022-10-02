import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
liq_list = list(map(int, input().split()))
liq_list.sort()

l = 0
r = N-1
res = sys.maxsize
resl = resr = 0

while l < r:
    if abs(liq_list[l] + liq_list[r]) == 0:
        resl = l
        resr = r
        break
    else:
        if res > abs(liq_list[l] + liq_list[r]):
            res = abs(liq_list[l] + liq_list[r])
            resl = l
            resr = r
        if liq_list[l] + liq_list[r] > 0:
            r -= 1
        else:
            l += 1

print(liq_list[resl], liq_list[resr])
