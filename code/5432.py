# 쇠막대기 자르기
# 5432.py

t = int(input())
for tc in range(1, t + 1):
    bar = input()

    stack = []
    result = 0 # 답
    i = 0

    for b in bar:
        if b == '(':
            stack.append(b)

        else: # ')'
            stack.pop() # stack 비었는지 확인 안해도 됨
            if tmp == '(': # 레이저 '()'
                result += len(stack)
            else: # 막대 끝
                result += 1
        tmp = b

    print('#{} {}'.format(tc, result))