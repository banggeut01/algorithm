# 5105.py 미로의 거리

import sys
import collections
sys.stdin = open('4875input.txt', 'r')


def bfs(i, j):
    dq = collections.deque()
    my_map[i][j] = 1
    dq.append((i, j))
    route = [[0] * n for _ in range(n)]

    # 상하좌우
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]

    while dq:
        a, b = dq.popleft() # 현재 위치
        for idx in range(4):
            row, col = a + x[idx], b + y[idx]
            if -1 < row < n and -1 < col < n:
                if my_map[row][col] == 0: # 인접 위치
                    my_map[row][col] = 1
                    dq.append((row, col))
                    route[row][col] = route[a][b] + 1
                elif my_map[row][col] == 3:
                    return route[a][b]
    return 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    my_map = [list(map(int, list(input()))) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 2:
                result = bfs(i, j)
                break

    print('#{} {}'.format(tc, result))
