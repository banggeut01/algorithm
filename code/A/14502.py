# 14502.py 연구소
from collections import deque
def getSet(k, s):
    if k == 3:
        global MAX
        # bfs
        dq = deque()
        visit = [[False] * M for _ in range(N)]
        for x in range(len(virus)):
            dq.append(virus[x])
            i, j = virus[x]
        while dq:
            i, j = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = i + dx, j + dy
                if -1 < nx < N and -1 < ny < M and not board[nx][ny] and not visit[nx][ny]:
                    dq.append((nx, ny))
                    visit[nx][ny] = True
        total = 0
        for i in range(N):
            for j in range(M):
                if not board[i][j] and not visit[i][j]:
                    total += 1
        MAX = max(MAX, total)
        return

    for x in range(s, len(candi)):
        wall.append(candi[x])
        i, j = candi[x]
        board[i][j] = 1
        getSet(k + 1, x + 1)
        wall.pop()
        board[i][j] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = deque()
candi = []
MAX = 0
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            candi.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
wall = []
getSet(0, 0)
print(MAX)