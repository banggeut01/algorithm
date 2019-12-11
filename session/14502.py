# 14502.py 연구소
from collections import deque
def bfs(x, y):
    dq = deque()
    for x, y in virus:
        dq.append((x, y))
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not board[nx][ny] and not visit[nx][ny]:
                dq.append((nx, ny))
                visit[nx][ny] = True
                cnt += 1
    return cnt

def getWall(k, s): # 벽 3개를 고름
    if k == 3:
        global MAX
        cnt = bfs(i, j) # empty -> virus 개수
        MAX = max(MAX, E - (cnt + 3))
        return

    for idx in range(s, E):
        x, y = empty[idx]
        board[x][y] = 1
        getWall(k + 1, idx + 1)
        board[x][y] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 0 빈칸, 1 벽, 2 바이러스
empty, virus = [], []
MAX = 0 # 안전 영역
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
E = len(empty)
getWall(0, 0)
print(MAX)