# 2110 공유기 설치 - 이분탐색, 매개변수 탐색
import sys

N, C = map(int, sys.stdin.readline().split())
home_list = sorted([int(sys.stdin.readline()) for _ in range(N)])
start = 1
end = max(home_list)

res = 0
while start <= end:
    mid = (end+start) // 2
    count = 1
    last_install = home_list[0]
    install_list = [last_install]

    for home in home_list:
        if (home - last_install) >= mid:
            last_install = home
            install_list.append(last_install)
            count += 1

    if C <= count:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
