# 2117.py [모의 SW 역량테스트] 홈 방범 서비스

def getServeCnt(i, j, x):
    cnt = 0
    nx, ny = i - x, j
    while nx <= i:
        if -1 < nx < N and -1 < ny < N and board[nx][ny]:
           cnt += 1
        nx, ny = nx + 1, ny - 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N:맵크기, M:집한채당 이익
    board = [list(map(int, input().split())) for _ in range(N)]
    H = 0 # 집 개수
    MAX = 0 # 최대 서비스 집 개수
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                H += 1
    # 최대 k구하기
    k = 1
    while H * M > k * k + (k + 1) * (k + 1):
        k += 1

    for i in range(N):
        for j in range(N):
            if board[i][j]: cnt = 1 # cnt: 서비스 집 개수
            else: cnt = 0
            for x in range(1, k):
                cnt += getServeCnt(i, j, x)