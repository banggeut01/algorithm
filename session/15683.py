# 15683.py 감시
def bf(k, total):
    if k == len(cctv):
        global MIN
        MIN = min(MIN, total)
        return

    x, y = cctv[k] # x, y에서 감시
    num = board[x][y] # cctv 번호
    for dirList in dir[num]:
        cnt = 0 # 감시 개수
        tmp = []
        for dirEl in dirList:
            dx, dy = D[dirEl]
            c = 0
            nx, ny = x + dx, y + dy
            while -1 < nx < N and -1 < ny < M and board[nx][ny] != 6:
                if not board[nx][ny]:
                    c += 1
                    board[nx][ny] = 7
                    tmp.append((nx, ny))
                nx, ny = nx + dx, ny + dy
            cnt += c
        bf(k + 1, total - cnt)
        for nx, ny in tmp:
            board[nx][ny] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
dir = [[],
     [[0], [1], [2], [3]],
     [[0, 1], [2, 3]],
     [[0, 3], [3, 1], [1, 2], [2, 0]],
     [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
     [[0, 1, 2, 3]]]
cctv = []
blind = 0 # 사각지대
MIN = 0xffffff # 답
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6: cctv.append((i, j))
        elif not board[i][j]: blind += 1
bf(0, blind)
print(MIN)