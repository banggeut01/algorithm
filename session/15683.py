# 15683.py 감시
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
dir = [[],
     [[0], [1], [2], [3]],
     [[0, 1], [2, 3]],
     [[0, 3], [3, 1], [1, 2], [2, 0]],
     [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
     [0, 1, 2, 3]]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            cctv.append((i, j))
