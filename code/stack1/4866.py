# 괄호검사 4866.py
t = int(input())
for tc in range(1, t + 1):
    cmd = input()
    stack = []
    for c in cmd:
        if c == '{' or c == '(':
            stack.append(c)
        elif c == '}' or c==')':
            # pop() 전에 Empty 주의!
            if len(stack) != 0:
                tmp = stack.pop()
                if c == '}' and tmp != '{':
                    result = 0
                    break
                elif c == ')' and tmp != '(':
                    result = 0
                    break
            else:
                result = 0
                break
    else:
        if len(stack) == 0:
            result = 1
        else:
            result = 0
    print('#{} {}'.format(tc, result))