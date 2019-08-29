T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    com = [list(map(int, input().split())) for _ in range(M)]
    board = [[0]*N for _ in range(N)]

    for x1, y1, x2, y2 in com:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1

    print('#{} {}'.format(t, cnt))

