# 2573.py 빙산

def dfs(i, j, visit):
    visit[i][j] = True
    for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = i + x, j + y
        if board[nx][ny] and not visit[nx][ny]:
            dfs(nx, ny, visit)

def meltIce():
    melt = [[0] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = i + x, j + y
                if not board[nx][ny]:
                    melt[i][j] += 1
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if melt[i][j]:
                if melt[i][j] >= board[i][j]: board[i][j] = 0
                else: board[i][j] -= melt[i][j]

def solution():
    rtn = 0
    while True:
        meltIce()
        flag = 0
        visit = [[False] * M for _ in range(N)]
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if board[i][j] and not visit[i][j]:
                    if not flag:
                        rtn += 1
                        flag = 1
                        dfs(i, j, visit)
                    else: # 두번째 섬
                        return rtn
        if not flag: # 다 녹았을 때
            rtn = 0
            return rtn

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 주변 0의 개수 melt

result = solution()
print(result)





