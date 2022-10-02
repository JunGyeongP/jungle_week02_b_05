import sys


def binary_search(home, start, end):
    result = 0
    if(C == 2):
        print(end)
    else:
        while start < end:
            mid = (start + end) // 2
            count = 1
            past_position = home[0]
            for i in range(N):
                if(home[i] - past_position >= mid):
                    count+= 1
                    past_position = home[i]
            if(count >= C):
                result = mid
                start = mid + 1
            elif count < C:
                end = mid
        print(result)
    
N, C = map(int, sys.stdin.readline().strip().split())
home = []
for i in range(N):
    home.append(int(sys.stdin.readline()))
home.sort()
start = 1
end = home[N-1] - home[0]
binary_search(home, start, end)
