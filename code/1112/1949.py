# 1949.py 등산로 조성

import sys
sys.stdin = open('1949input.txt', 'r')
def dfs(x, y, d):
    global result, flag
    result = max(result, d)

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
            if board[nx][ny] < board[x][y]:
                visit[nx][ny] = True
                dfs(nx, ny, d + 1)
                visit[nx][ny] = False
            else:
                if flag: continue
                for h in range(1, K + 1):
                    board[nx][ny] -= h
                    if board[nx][ny] < board[x][y]:
                        visit[nx][ny] = True
                        flag = 1
                        dfs(nx, ny, d + 1)
                        visit[nx][ny] = False
                        flag = 0
                    board[nx][ny] += h

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    start, maxNum = [], 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > maxNum:
                start = []
                maxNum = board[i][j]
                start.append((i, j))
            elif board[i][j] == maxNum:
                start.append((i, j))
    while start:
        visit = [[False] * N for _ in range(N)]
        flag = 0
        i, j = start.pop()
        visit[i][j] = True
        dfs(i, j, 1)
    print('#{} {}'.format(tc, result))