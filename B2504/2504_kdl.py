words = input()
stk = []
pt = 0
tmp = 1
for i in range(len(words)):
    if words[i] == '(':
        stk.append(words[i])
        tmp *= 2
    elif words[i] == '[':
        stk.append(words[i])
        tmp *= 3
    elif words[i] == ')':
        if not stk or stk[-1] == '[':
            pt = 0
            break
        if words[i-1] == '(':
            pt += tmp
        stk.pop()
        tmp //= 2
    else:
        if not stk or stk[-1] == '(':
            pt = 0
            break
        if words[i-1] == '[':
            pt += tmp
        stk.pop()
        tmp //= 3

if stk:
    pt = 0
print(pt)
