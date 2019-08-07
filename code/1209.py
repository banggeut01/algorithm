# 1209.py 2일차 - Sum
import sys
sys.stdin = open('1209input.txt', 'r')

for _ in range(10):
    tc = input()

    # arr = [list(map(int, input().split())) for _ in range(100)] # => 2차원 리스트
    arr = []
    for _ in range(100):
        arr += list(map(int, input().split()))

    # 최대 합 초기화(1행 합)
    max_sum = 0
    for i in range(100):
        max_sum += arr[i]

    # 행 합
    for row in range(1, 100): # 행 1 ~ 99
        tmp = 0 # 행의 합 임시저장변수
        for col in range(100): # 열 0 ~ 99
            tmp += arr[100*row + col]
        if tmp > max_sum:
            max_sum = tmp

    # 열 합
    for col in range(100): # 열
        tmp = 0
        for row in range(100):
            tmp += arr[100*row + col]
        if tmp > max_sum:
            max_sum = tmp

    # 대각선 0,0 -> ... -> 99, 99
    tmp = 0
    for i in range(100):
        tmp += arr[100*i + i]
    if tmp > max_sum:
        max_sum = tmp

    # 대각선 0,99 -> 1,98 -> 2, 97 -> ...-> 99, 0
    tmp = 0
    for i in range(100):
        tmp += arr[100*i + 99 - i]
    if tmp > max_sum:
        max_sum = tmp

    print('#{} {}'.format(tc, max_sum))