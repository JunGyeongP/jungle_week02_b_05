n = input()
stack = []
tmp = 1
res = 0

for i in range(len(n)):
  if (n[i] == '('):
    tmp *= 2
    stack.append(n[i])
  elif n[i] == '[':
    tmp *= 3
    stack.append(n[i])

  elif (n[i] == ')'):
    if not stack or stack[-1] == '[': #스택이 비지 않았거나 [) 조합이 나올 경우
      res = 0
      break
    if n[i-1] == '(': #() 조합이 될 경우
      res += tmp
    tmp //= 2
    stack.pop() # pop도 까먹지 말고 꼭
  
  else:
    if not stack or stack[-1] == '(':
      res = 0
      break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님
    if n[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop()

if stack: #스택에 남는 값들(짝이 없는 괄호)가 있을 경우
  res = 0
print(res)