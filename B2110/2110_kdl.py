import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bin_search():
    N, C = map(int, input().split())
    house = [int(input()) for _ in range(N)]
    house.sort()

    result = 0
    minV = 1
    maxV = house[N-1] - house[0]

    if N == 2:
        return maxV
    else:
        while minV <= maxV:
            cnt = 1
            midV = (maxV + minV) // 2
            st_house = house[0]
            for i in range(1, (len(house))):
                if house[i] - st_house >= midV:
                    st_house = house[i]
                    cnt += 1
            if cnt < C:
                maxV = midV-1
            else:
                result = midV
                minV = midV+1
    return result


print(bin_search())
