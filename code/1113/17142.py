# 17142.py 연구소3

from collections import deque
# 빈칸 바이러스 퍼지는 개수, 빈칸 바이러스 거리 계산해야!
def bfs():
    global MIN

    dq = deque()
    visit = [[False] * N for _ in range(N)]
    D = [[0] * N for _ in range(N)]
    cnt = 0 # 빈칸 -> 바이러스 개수
    for idx in range(M):
        dq.append(active[idx])
        x, y = active[idx]
        visit[x][y] = True
    maxD = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
                if not board[nx][ny]: # 빈칸
                    visit[nx][ny] = True
                    dq.append((nx, ny))
                    D[nx][ny] = D[x][y] + 1
                    maxD = max(maxD, D[nx][ny])
                    cnt += 1
                elif board[nx][ny] == 2 and not (nx, ny) in active: # 비활성 -> 활성
                    visit[nx][ny] = True
                    dq.append((nx, ny))
                    D[nx][ny] = D[x][y] + 1
    if cnt == EMPTY:
        if MIN != -1: MIN = min(MIN, maxD)
        else: MIN = maxD

def getActiveSet(k, s):
    if k == M:
        bfs()
        return

    for idx in range(s, len(virus)):
        active.append(virus[idx])
        getActiveSet(k + 1, idx + 1)
        active.pop()

N, M = map(int, input().split()) # N:연구소크기, M:바이러스개수
board = [list(map(int, input().split())) for _ in range(N)] #0빈칸,1벽,2바이러스
virus = [] # 바이러스
EMPTY = 0 # 0(빈칸) 개수
for i in range(N):
    for j in range(N):
        if board[i][j] == 2: virus.append((i, j))
        elif not board[i][j]: EMPTY += 1
active = []
MIN = -1

getActiveSet(0, 0)
print(MIN)
