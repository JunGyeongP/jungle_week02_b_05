import sys

M, N, L = map(int, sys.stdin.readline().strip().split())
killC = 0
sasu = list(map(int, sys.stdin.readline().strip().split()))
sasu.sort()

for i in range(N):
    x, y = map(int,sys.stdin.readline().strip().split())

    if(y > L): 
        continue
    
    lower = x+y-L
    upper = x-y+L

    left = 0
    right = len(sasu)-1
    while(left <= right):
        mid = (left+right)//2

        if(lower <= sasu[mid] and sasu[mid] <= upper):
            killC+= 1
            break
        elif(sasu[mid]<lower):
            left = mid+1
        elif(upper < sasu[mid]):
            right = mid -1


print(killC)