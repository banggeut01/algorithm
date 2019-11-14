# 5653.py [모의 SW 역량테스트] 줄기세포배양
import sys
sys.stdin = open('5653input.txt', 'r')

from collections import deque

def bfs():
    visitList = []
    tmpList = []
    t = 2
    while dq and t < K + 1: # 2~K 시간동안
        if dq[0][0] > t:
            # visit 표시
            while visitList:
                x, y = visitList.pop()
                visit[x][y] = True
            t += 1
            while tmpList:
                dq.appendleft(tmpList.pop())
            continue
        breedT, meT, deadT, x, y = dq.popleft() # breedT번식시간, meT자신시간, deadT죽는시간, xy좌표
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if not visit[nx][ny] and not board[nx][ny] and not (nx, ny) in visitList:
                tmp = t + meT + 1 # 번식가능시간: 현재t+자신T+1
                idx = 0
                while idx < len(dq) and dq[idx][0] < tmp :
                    idx += 1
                if idx < len(dq) and dq[idx][0] == tmp:
                    while idx < len(dq) and dq[idx][0] == tmp and \
                            dq[idx][1] > meT:
                        idx += 1
                dq.insert(idx, (tmp, meT, tmp + meT, nx, ny))
                visitList.append((nx, ny))
        if deadT > t: tmpList.append((breedT, meT, deadT, x, y))
    cnt = 0
    for x in range(len(dq)):
        if dq[x][2] > t: cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # N:세로, M:가로, K:배양시간
    inputBoard = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * 700 for _ in range(700)]
    dq = deque()
    visit = [[False] * 700 for _ in range(700)]

    # (( 번식타임(현재T+자신T+1), 자신T, 좌표ij
    # visit 표시 T 단계마다 하기
    # visit 나중에 표시하기
    for i in range(N):
        for j in range(M):
            if inputBoard[i][j]:
                board[300 + i][300 + j] = inputBoard[i][j]
                visit[300 + i][300 + j] = True
                if not dq:
                    dq.append((inputBoard[i][j] + 1, inputBoard[i][j], inputBoard[i][j] + 1 + inputBoard[i][j], i + 300, j + 300))
                else:
                    idx = 0
                    while idx < len(dq) and dq[idx][1] <= inputBoard[i][j]:
                        idx += 1
                    dq.insert(idx, (inputBoard[i][j] + 1, inputBoard[i][j], inputBoard[i][j] + 1 + inputBoard[i][j], i + 300, j + 300))
    result = bfs()
    print('#{} {}'.format(tc, result))
