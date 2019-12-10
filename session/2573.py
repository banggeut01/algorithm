# 2573.py 빙산
from collections import deque
def getWaterCnt(x, y): # 인접 호수 개수
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and not board[nx][ny]:
            melt[x][y] += 1

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and board[nx][ny] and not visit[nx][ny]:
                dq.append((nx, ny))
                visit[nx][ny] = True

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
year = 0
while True:
    year += 1
    melt = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                getWaterCnt(i, j)
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                board[i][j] = max(0, board[i][j] - melt[i][j])
    cnt = 0 # 덩어리 개수
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                cnt += 1
                bfs(i, j)
    if cnt >= 2: print(year); break
    elif cnt == 0: print(0); break

