# 2636.py 치즈

import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    visit[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and not visit[nx][ny]:
            if board[nx][ny]:
                visit[nx][ny] = True
                melt.append((nx, ny))
            else:
                dfs(nx, ny)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    visit = [[False] * M for _ in range(N)]
    melt = []
    dfs(0, 0)
    if not len(melt):
        break
    time += 1
    tmp = len(melt)
    while melt:
        x, y = melt.pop()
        board[x][y] = 0
print(time)
print(tmp)

