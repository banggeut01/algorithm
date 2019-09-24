# 반복문자 지우기 4873.py
t = int(input())

for tc in range(1, t + 1):
    word = input()
    stack = []

    top = -1

    for char in word:
        if top != -1 and stack[top] == char:
            stack.pop()
            top -= 1
        else:
            stack.append(char)
            top += 1

    print('#{} {}'.format(tc, len(stack)))




