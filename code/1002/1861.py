# 1861.py 정사각형 방


def back(i, j, v, k): # 좌표, 현재값, K번째
    global CNT, ANS
    if k > CNT:
        CNT = k
        ANS = v
    elif k == CNT:
        ANS = min(ANS, v)
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        r, c = i + dx, j + dy
        if -1 < r < N and -1 < c < N and board[r][c] == board[i][j] + 1:
            back(r, c, v, k + 1)

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    CNT, ANS = 0, 0 # 이동횟수, 방번호

    for i in range(N):
        for j in range(N):
            back(i, j, board[i][j], 1)
    print('#{} {} {}'.format(tc, ANS, CNT))