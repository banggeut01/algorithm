# 금속막대 1259.py
import sys
sys.stdin = open('1259input.txt', 'r')

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    screw = list(map(int, input().split()))
    result = []

    # 시작 나사 찾기
    for k in range(n): # screw[2*k] 수나사
        for i in range(n):
            if screw[2*i+1] == screw[2*k]: # 매칭되는 암나사 찾으면,
                break
        else:
            start = 2*k # 시작 나사
            break

    result.append(screw[start])
    result.append(screw[start + 1])

    for _ in range(n-2):
        for k in range(n): # result[-1]: 암나사
            if result[-1] == screw[2 * k]:
                result.append(screw[2 * k])
                result.append(screw[2 * k + 1])

    result = map(str, result)
    print('#{} {}'.format(tc, ' '.join(result)))