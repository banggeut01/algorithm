# 14890.py 경사로


def isRowPossible(i, j):
    prev = board[i][j]
    for j in range(1, N):
        if board[i][j] != prev:
            if abs(board[i][j] - prev) != 1: return False
            if board[i][j] > prev:
                nj = j
                for nj in range(j - 1, j - L - 1, -1):
                    if 0 > nj: return False
                    if board[i][nj] != board[i][j - 1]: return False
                    if visit[0][i][nj]: return False
                    visit[0][i][nj] = True
                # if 0 < nj and board[i][nj - 1] != board[i][j - 1]: return False
            if board[i][j] < prev:
                nj = j
                for nj in range(j, j + L, 1):
                    if nj >= N: return False
                    if board[i][nj] != board[i][j]: return False
                    if visit[0][i][nj]: return False
                    visit[0][i][nj] = True
                # if nj + 1 < N and board[i][nj + 1] != board[i][j]: return False
        prev = board[i][j]
    return True

def isColPossible(i, j):
    prev = board[i][j]
    for i in range(1, N):
        if board[i][j] != prev:
            if abs(board[i][j] - prev) != 1: return False
            if board[i][j] > prev:
                ni = i
                for ni in range(i - 1, i - L - 1, -1):
                    if 0 > ni: return False
                    if board[ni][j] != board[i - 1][j]: return False
                    if visit[1][ni][j]: return False
                    visit[1][ni][j] = True
                # if 0 < ni and board[i][ni - 1] != board[i - 1][j]: return False
            if board[i][j] < prev:
                ni = i
                for ni in range(i, i + L, 1):
                    if ni >= N: return False
                    if board[ni][j] != board[i][j]: return False
                    if visit[1][ni][j]: return False
                    visit[1][ni][j] = True
                # if ni + 1 < N and board[ni + 1][j] != board[i][j]: return False
        prev = board[i][j]
    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[[False] * N for _ in range(N)] for _ in range(2)] # visit[0][i][j]행, visit[1][i][j]열
result = 0
# 가로만
for i in range(N):
    if isRowPossible(i, 0): result += 1
    if isColPossible(0, i): result += 1
print(result)