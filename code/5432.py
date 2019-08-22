# 쇠막대기 자르기
# 5432.py

t = int(input())
for tc in range(1, t + 1):
    bar = input()

    stack = []
    result = 0 # 답
    cnt = 0 # 막대기 개수 임시 저장
    for b in bar:
        if b == '(': # 입력값 '('
            if stack and not stack[-1]: # 막대기 끝 만났을 때, ')('
                result += 1
            stack.append(b)
            cnt += 1
            tmp = 1 # tmp 이전 괄호 1:'(', 0:')'
        else: # 입력값 ')'
            if tmp: # 레이저 쐈을 때, '()',
                cnt -= 1
                result += cnt
                stack.pop()
            elif stack:
                if stack[-1] == b: # '))'
                    stack.append(b)
                else: # '()'
                    stack.pop()
                cnt -= 1
            tmp = 0

    print(result)