dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def limit(x, y):
    if 0 <= x < N and 0 <= y < N:
        return 1
    else:
        return 0


def dfs(x, y):
    visit[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if limit(nx, ny) and not visit[nx][ny] and board[nx][ny]:
            dfs(nx, ny)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j]:
                cnt += 1
                dfs(i, j)

    print('#{} {}'.format(t, cnt))
