# 2117_fail.py [모의 SW 역량테스트] 홈 방범 서비스

import sys
sys.stdin = open('2117input.txt', 'r')

def getServeCnt(i, j, x):
    cnt = 0
    nx, ny = i - x, j
    while nx + 1 <= i:
        nx, ny = nx + 1, ny - 1
        if -1 < nx < N and -1 < ny < N and board[nx][ny]:
           cnt += 1
    while ny + 1 <= j:
        nx, ny = nx + 1, ny + 1
        if -1 < nx < N and -1 < ny < N and board[nx][ny]:
            cnt += 1
    while nx - 1 >= i:
        nx, ny = nx - 1, ny + 1
        if -1 < nx < N and -1 < ny < N and board[nx][ny]:
            cnt += 1
    while ny - 1 >= j:
        nx, ny = nx - 1, ny - 1
        if -1 < nx < N and -1 < ny < N and board[nx][ny]:
            cnt += 1
    return cnt


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
    maxK = 1
    while H * M > (maxK + 1) **2 + maxK ** 2:
        maxK += 1

    for i in range(N):
        for j in range(N):
            if board[i][j]: # 서비스 영역의 중심위치 (i, j)
                cnt = 1  # cnt: 서비스 집 개수
                if M > 1: MAX = max(MAX, cnt)  # cnt: 1
            else: cnt = 0
            for k in range(1, maxK): # K = 2, 3,... 일 때 k = 1, 2,...
                cnt += getServeCnt(i, j, k)
                if cnt * M >= (k + 1) **2 + k ** 2: # 수익 - 운영 비용
                    MAX = max(MAX, cnt)

    print('#{} {}'.format(tc, MAX))