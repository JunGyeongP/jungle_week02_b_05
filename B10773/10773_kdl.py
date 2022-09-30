import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

K = int(input())
order_list = [int(input()) for _ in range(K)]
stk = []

for order in order_list:
    if order == 0:
        stk.pop()
    else:
        stk.append(order)

print(sum(stk))
