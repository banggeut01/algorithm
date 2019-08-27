# 1224.py 계산기3

import sys
sys.stdin = open('1224input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    stack = []
    postfix = []
    infix = input()

    # 중위 => 후위
    for c in infix:
        if c == '(':
            stack.append('(')
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop() # '(' pop()
            if stack:
                postfix.append
        elif c == '*': # 연산자
            stack.append(c)
        elif c == '+': # 연산자
            while stack and stack[-1] == '*':
                postfix.append(stack.pop())
            stack.append(c)
        else: # 피연산자
            postfix.append(c)

    # 후위표기식 계산
    for c in postfix:
        if c == '+':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num1 + num2)
        elif c == '*':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num1 * num2)
        else: # 피연산자
            stack.append(c)
    result = stack.pop()
    print('#{} {}'.format(tc, result))