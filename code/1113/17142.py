# 17142.py 연구소3


def getActiveSet(k, s):
    
N, M = map(int, input().split()) # N:연구소크기, M:바이러스개수
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2: virus.append((i, j))
        elif not board[i][j]: empty += 1
active = []
getActiveSet(0, 0)