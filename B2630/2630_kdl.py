import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

white_num = 0
blue_num = 0


def check(start_row, start_col, n):
    curr_color = paper[start_row][start_col]
    global white_num, blue_num

    for i in range(start_row, start_row+n):
        for j in range(start_col, start_col+n):
            if curr_color != paper[i][j]:
                next_n = n // 2
                check(start_row, start_col, next_n)
                check(start_row, start_col+next_n, next_n)
                check(start_row+next_n, start_col, next_n)
                check(start_row+next_n, start_col+next_n, next_n)
                return
    if curr_color == 0:
        white_num += 1
    else:
        blue_num += 1


check(0, 0, N)
print(white_num)
print(blue_num)
