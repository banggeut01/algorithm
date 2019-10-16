# 13459.py 구슬 탈출
def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x + dx][y + dy] != 'O':
        x, y = x + dx, y + dy
        cnt += 1
    return (x, y, cnt)
def bfs():
    while dq:
        rx, ry, bx, by, dist = dq.popleft()
        if dist == 10:
            return 0
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nrx, nry, rc = move(rx, ry, dx, dy)
            # if rc == 0: continue # R이 이동한 거리가 0이다. => 빼야함 R과 O 인접인 경우
            nbx, nby, bc = move(bx, by, dx, dy)
            rf, bf = 0, 0
            if board[nrx + dx][nry + dy] == 'O': rf = 1 # R구멍
            if board[nbx + dx][nby + dy] == 'O': bf = 1# B구멍
            if bf == 1: continue # B가 들어감
            if rf == 1: return 1 # R만 들어감
            if nrx == nbx and nry == nby: # 같은 좌표
                if rc < bc: nbx, nby = nbx - dx, nby - dy
                else: nrx, nry = nrx - dx, nry - dy
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                dq.append((nrx, nry, nbx, nby, dist + 1))
    return 0

from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ANS = 0
# 갈수 있는 조건: '#'가 아니고 , 'O'가 아니고
dq = deque()
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dq.append((rx, ry, bx, by, 0))
visit[rx][ry][bx][by] = True
result = bfs()
print(result)