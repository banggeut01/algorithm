# 14499.py 주사위 굴리기

# cu = [[0, 2, 0],
#       [4, 1, 3],
#       [0, 5, 0],
#       [0, 6, 0]]
cu = [[0] * 3 for _ in range(4)]
# 1: 동, 2: 서, 3: 북, 4: 남
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
for c in cmd:
    nx, ny = x + d[c][0], y + d[c][1]

    if -1 < nx < N and -1 < ny < M:
        # 주사위 굴리기
        if c == 4: # 남
            cu[0][1], cu[1][1], cu[2][1], cu[3][1] = cu[3][1], cu[0][1], cu[1][1], cu[2][1]
        elif c == 3: # 북
            cu[0][1], cu[1][1], cu[2][1], cu[3][1] = cu[1][1], cu[2][1], cu[3][1], cu[0][1]
        elif c == 2: # 서
            cu[1][0], cu[1][1], cu[1][2], cu[3][1] = cu[1][1], cu[1][2], cu[3][1], cu[1][0]
        else: # 동
            cu[1][0], cu[1][1], cu[1][2], cu[3][1] = cu[3][1], cu[1][0], cu[1][1], cu[1][2]
        if not board[nx][ny]: # 주사위 바닥 => 칸,
            board[nx][ny] = cu[3][1]
        else: # 칸 => 주사위 바닥, 칸 = 0
            cu[3][1], board[nx][ny] = board[nx][ny], 0
        # print(c, cu[1][1], nx, ny)
        x, y = nx, ny
        print(cu[1][1])
