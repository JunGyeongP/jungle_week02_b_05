import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def f_tower():
    N = int(input())
    towers = list(map(int, input().split()))
    stk = []
    ans = []
    for i in range(len(towers)):
        while stk:
            if stk[-1][0] >= towers[i]:
                ans.append(stk[-1][1]+1)
                break
            else:
                stk.pop()
        if not stk:
            ans.append(0)
        stk.append([towers[i], i])

    print(*ans)


f_tower()
