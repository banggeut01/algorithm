# 회문2 1216.py
import sys


def row_pal(i, j, m):
    p = 0 # p: 회문 idx
    while p < m // 2:
        if word[i][j + p] == word[i][j + m - p - 1]:
            p += 1
        else:
            return 1
    return m

def col_pal(i, j, m):
    p = 0 # p: 회문 idx
    while p < m // 2:
        if word[i + p][j] == word[i + m - p - 1][j]:
            p += 1
        else:
            return 1
    return m

sys.stdin = open('1216input.txt', 'r')
for t in range(10):
    tc = int(input())
    word = [input() for _ in range(100)]

    max_len = 0
    for i in range(100):
        for j in range(99): # j인덱스 0 ~ 98
            for m in range(100-j, 1, -1): # 회문 길이 100 ~ 2, 길이1이면 1출력
                tmp = row_pal(i, j, m)
                if tmp > max_len:
                    max_len = tmp
                tmp = col_pal(j, i, m)
                if tmp > max_len:
                    max_len = tmp

    print('#{} {}'.format(tc, max_len))



