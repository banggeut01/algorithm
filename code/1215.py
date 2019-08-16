# 회문1 1215.py

# import sys

def row_pal(i, j, m):
    p = 0 # p: 회문 idx
    while p < m // 2:
        if word[i][j + p] == word[i][j + m - p - 1]:
            p += 1
        else:
            return False
    return True

def col_pal(i, j, m):
    p = 0 # p: 회문 idx
    while p < m // 2:
        if word[i + p][j] == word[i + m - p - 1][j]:
            p += 1
        else:
            return False
    return True

# sys.stdin = open('1215input.txt', 'r')
for tc in range(1, 11):
    m = int(input())
    word = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(9 - m): # word길이 - m까지
            if row_pal(i, j, m):
                cnt += 1
            if col_pal(j, i, m):
                cnt += 1
    print('#{} {}'.format(tc, cnt))