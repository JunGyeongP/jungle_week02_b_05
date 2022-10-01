import sys
T = int(sys.stdin.readline())

for _ in range(T):
    word = sys.stdin.readline().strip()
    li = []
    for w in word:
        if w == "(":
            li.append(w)
        elif w == ")" and not li:
            print("NO")
            break
        else:
            li.pop()
    else:
        if not li:
            print("YES")
        else:
            print("NO")
