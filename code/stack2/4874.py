# 4874.py Forth

t = int(input())

for tc in range(1, t + 1):
    postfix = list(input().split())
    stack = []
    operator = ['+', '-', '*', '/']

    for c in postfix:
        if c.isdigit():
            stack.append(int(c))
        elif c in operator:
            # 피연산자2 pop
            if stack:
                num2 = stack.pop()
            else:
                result = 'error'
                break
            # 피연산자1 pop
            if stack:
                num1 = stack.pop()
            else:
                result = 'error'
                break
            # 연산 수행
            if c == '+':
                stack.append(num1 + num2)
            elif c == '*':
                stack.append(num1 * num2)
            elif c == '-':
                stack.append(num1 - num2)
            else: # '/'
                stack.append(num1 // num2)
        elif c == '.':
            if stack:
                result = stack.pop()
                break
            else:
                result = 'error'
                break
        else: # 다른 문자열
            result = 'error'
            break

    if stack:
        result = 'error'

    print('#{} {}'.format(tc, result))