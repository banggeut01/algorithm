# 2468.py 안전영역
import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    visit[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and board[nx][ny] > h and not visit[nx][ny]:
            dfs(nx, ny)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 1
maxH = 1
for i in range(N):
        maxH = max(maxH, max(board[i]))
for h in range(1, maxH): # 비높이 1 ~ maxH-1
    cnt = 0 # 높이 h일때 안전영역개수
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visit[i][j]:
                cnt += 1
                dfs(i, j)
    result = max(result, cnt)
print(result)