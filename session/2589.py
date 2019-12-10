# 2589.py 보물섬
from collections import deque
def bfs(x, y):
    visit = [[False] * M for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append((x, y))
    visit[x][y] = True
    maxD = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and board[nx][ny] == 'L' and not visit[nx][ny]:
                dq.append((nx, ny))
                visit[nx][ny] = True
                D[nx][ny] = D[x][y] + 1
                maxD = D[nx][ny]
    return maxD

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
