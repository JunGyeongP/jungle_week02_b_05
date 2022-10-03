import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
stk = []
for i in list(map(int, input().split())):
    if not stk:
        print(0)
    else:
        isSet = False
        for j in range(len(stk)-1, 0, -1):
            if stk[j] >= i:
                isSet = True
                print(j+1)
                break
        if isSet == False:
            print(0)
    stk.append(i)
