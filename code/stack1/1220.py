import sys

sys.stdin = open('1220input.txt', 'r')


def magnetic(j):
    cnt = 0
    state = 0
    for i in range(n):
        if table[i][j] == 2 and state == 1:
            cnt += 1
        if table[i][j] != 0: # 0일 때, 상태변화하면 안됨!
            state = table[i][j]
    return cnt


for tc in range(1, 11):
    n = int(input())  # n:테이블크기 n*n테이블

    # 1: N극, 2: S극 / N극 상단, S극 하단
    table = [list(map(int, input().split())) for _ in range(100)]

    result = 0  # 답
    for col in range(n):  # 열
        result += magnetic(col)

    print('#{} {}'.format(tc, result))