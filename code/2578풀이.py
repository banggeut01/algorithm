# 2578풀이.py
import sys
sys.stdin = open('1209input.txt', 'r')

for tc in range(1, 11):

    arr = [list(map(int, input().split())) for _ n range(100)]

    max_num = 0 # 최대값(답)


    # for문 한개쓰기
    dsum1 = dsum2 = 0# 대각 순회 합
    for i in range(100):
        rs = cs = 0 # 행, 열 우선순회 합
        dsum1 += arr[i][i]
        dsum2 += arr[i][99 - i]
        for j in range(100):
            s += arr[i][j]
            s += arr[i][j]
        max_num = max(max_num, rs, cs, dsum1, dsum2)


'''
    # 행 우선 순회
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]
        max_num = max(max_num, s)
    # 열 우선 순회
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[j][i]
        max_num = max(max_num, s)
    # 대각 순회
    s = 0
    for i in range(100):
        s += arr[i][i]
    max_num = max(max_num, s)

    s = 0
    for i in range(100):
        s += arr[i][99 - i]
    max_num = max(max_num, s)
'''