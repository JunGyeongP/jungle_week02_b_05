import sys
def HOS(start, end, levels):
    T = 0
    while start <= end:
        mid = (start + end) // 2
        
        hap = 0
        for level in levels:
            if mid > level:
                hap += (mid - level)
            
        if hap <= K:
            start = mid+1
            T = max(mid,T)
        else:
            end = mid -1
    return(T)

N, K = map(int, sys.stdin.readline().strip().split())
levels = []
for i in range(N):
    levels.append(int(sys.stdin.readline()))

start = min(levels)
end = start + K

print(HOS(start, end, levels))