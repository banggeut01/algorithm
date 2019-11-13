# 5656.py [모의 SW 역량테스트] 벽돌 깨기

import sys, pprint
sys.stdin = open('5656input.txt', 'r')
import copy
from collections import deque
def breakBox(x, y, copied): # x, y 현재 좌표, copied : 맵
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        size = copied[x][y]
        copied[x][y] = 0
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1): # 네방향에 대해
            nx, ny = x, y
            i = 0
            while i < size - 1:
                nx, ny = nx + dx, ny + dy
                if -1 < nx < W and -1 < ny < len(copied[nx]):
                    if copied[nx][ny] == 1:
                        copied[nx][ny] = 0
                    elif copied[nx][ny] > 1:
                        dq.append((nx, ny))
                i += 1
        copied[x][y] = 0
    for x in range(W):
        y = 0
        while y < len(copied[x]):
            if not copied[x][y]: copied[x].pop(y)
            else:
                y += 1

def getRemainCnt(copied): # 남은 벽돌수
    cnt = 0
    for x in range(W):
        cnt += len(copied[x])
    return cnt

def perm(k):
    global cntOfMaxBreakBox
    if k == N:
        global MIN
        copied = copy.deepcopy(queueBoard)
        for idx in range(N): # N개의 폭탄 터트리는데,
            i = seq[idx] # seq[idx] 터트릴 벽돌의 행위치
            for j in range(len(copied[i]) - 1, -1, -1): # 열위치 => copied[i][j]: 제거할 벽돌 위치
                if copied[i][j] == 1:
                    copied[i].pop()
                    break
                elif copied[i][j] > 1:
                    breakBox(i, j, copied) # 벽돌 깨기
                    break
        MIN = min(MIN, getRemainCnt(copied))
        return

    for j in range(W):
        seq.append(j)
        perm(k + 1)
        seq.pop()

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split()) # N:벽돌개수, W:너비, H:높이
    board = [list(map(int, input().split())) for _ in range(H)]
    queueBoard = [[] for _ in range(W)]
    for i in range(H - 1, -1, -1):
        for j in range(W):
            if board[i][j]:
                queueBoard[j].append(board[i][j])
    seq = []
    MIN = W * H
    perm(0)
    print('#{} {}'.format(tc, MIN))
