import sys
K = int(sys.stdin.readline())
li = []
for _ in range(K):
    e = int(sys.stdin.readline())
    if e == 0:
        li.pop()
    else:
        li.append(e)
print(sum(li))
