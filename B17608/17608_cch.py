import sys
N = int(sys.stdin.readline())
bar_stack = [int(sys.stdin.readline()) for _ in range(N)]

last_bar = bar_stack.pop()
count = 1
for _ in range(N-1):
    now_bar = bar_stack.pop()
    if last_bar < now_bar:
        count += 1
        last_bar = now_bar
print(count)
