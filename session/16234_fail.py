# 16234_fail.py 인구이동 DFS
def dfs(x, y):
    visit[x][y] = True
    tmp.append((x, y))
    ret = board[x][y]
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny] \
            and L <= abs(board[nx][ny] - board[x][y]) <= R:
            ret += dfs(nx, ny)
    return ret

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0 # 인구이동 횟수
while True:
    cnt = 0  # 연합 개수
    flag = False
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                tmp = []
                cnt += 1
                total = dfs(i, j)
                if len(tmp) > 1:
                    flag = True
                    newVal = total // len(tmp)
                    while tmp:
                        i, j = tmp.pop()
                        board[i][j] = newVal
    if flag: # 인구 이동
        result += 1
    else:
        break
print(result)