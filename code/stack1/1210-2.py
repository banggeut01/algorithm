# Ladder1 1210,1210-2.py
# 재귀를 사용하여 해보자.

import sys
sys.stdin = open('1210input.txt', 'r')

def ladder(i, j):
    visit[i][j] = True

    if i == 0:
        return j

    if j != 0 and grid[i][j - 1] and not visit[i][j - 1]:
        return ladder(i, j - 1)
    elif j != 99 and grid[i][j + 1] and not visit[i][j + 1]:
        return ladder(i, j + 1)
    else:
        return ladder(i - 1, j)


for _ in range(10):
    tc = input()
    grid = [list(map(int, input().split())) for _ in range(100)]
    visit = [[False] * 100 for _ in range(100)]

    for j in range(100): # 열
        if grid[99][j] == 2:
            break

    result = ladder(99, j)
    print('#{} {}'.format(tc, result))
