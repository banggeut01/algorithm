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
            # stack 비었는지 확인 안해도 됨
            stack.pop()
            result += len(stack)
        # i += 1
        # print(i, result)
        # print('{} {}'.format(i, stack))
    print('#{} {}'.format(tc, result))