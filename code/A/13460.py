# 13460.py 구슬 탈출2
from collections import deque

def move(x, y, dx, dy):
    c = 0
    while board[x + dx][y + dy] != '#' and board[x + dx][y + dy] != 'O':
        x, y = x + dx, y + dy
        c += 1
    return (x, y, c)

def bfs():
    while dq:
        rx, ry, bx, by, dist = dq.popleft() # r좌표, b좌표, 거리
        if dist == 10: return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nrx, nry, rcnt = move(rx, ry, dx, dy)
            nbx, nby, bcnt = move(bx, by, dx, dy)
            if board[nbx + dx][nby + dy] == 'O': continue # B 구멍으로
            if board[nrx + dx][nry + dy] == 'O': # R만 구멍으로
                global ANS
                ANS = dist + 1
                return
            if nrx == nbx and nry == nby: # 같은 좌표
                if rcnt > bcnt: nrx, nry = nrx - dx, nry - dy
                else: nbx, nby = nbx - dx, nby - dy
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                dq.append((nrx, nry, nbx, nby, dist + 1))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dq = deque()
visit[rx][ry][bx][by] = True
dq.append((rx, ry, bx, by, 0))
ANS = -1
bfs()
print(ANS)