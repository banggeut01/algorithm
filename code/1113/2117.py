# 2117.py [모의 SW 역량테스트] 홈 방범 서비스 BFS

import sys
sys.stdin = open('2117input.txt', 'r')
from collections import deque
def bfs(i, j):
    if board[i][j]: cnt = 1
    else: cnt = 0
    visit = [[False] * N for _ in range(N)]
    D = [[0] * N for _ in range(N)]
    D[i][j] = 1
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    prevK = 0
    while dq:
        x, y = dq.popleft()
        if D[x][y] != prevK: # k값 변했을 때,
            if cnt * M >= D[x][y] ** 2 + (D[x][y] - 1) ** 2: # 손실 아닐 때
                global MAX
                MAX = max(MAX, cnt)
            prevK = D[x][y]
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
                if D[x][y] + 1 > maxK: return # 제한 k 초과
                if board[nx][ny]: cnt += 1
                D[nx][ny] = D[x][y] + 1
                visit[nx][ny] = True
                dq.append((nx, ny))

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
            # 서비스 영역의 중심위치 (i, j)
            bfs(i, j)

    print('#{} {}'.format(tc, MAX))
