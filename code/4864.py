# 문자열 비교 4864.py

t = int(input())

for tc in range(1, t+1):
    p = input() # pattern, 길이 m
    t = input() # text, 길이 n
    n, m = len(t), len(p)

    i = j = 0 # i: t의 idx, j: p의 idx
    while i < n and j < m:
        if t[i] == p[j]: # 문자 일치
            i += 1
            j += 1
        else: # 일치하지 않으면,
            i = i - j + 1 # 시작위치 다음으로
            j = 0


    if j == m:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

