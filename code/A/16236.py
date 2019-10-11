# 16236.py 아기 상어

import collections
def bfs(i, j):
    s = 2 # 크기
    t = 0
    cnt = 0  # 잡아먹은 물고기 수
    while True:
        dq = collections.deque()
        visit = [[False] * N for _ in range(N)]
        D = [[0] * N for _ in range(N)]
        dq.append((i, j))
        dist = 0
        visit[i][j] = True
        initi, initj = ni, nj = i, j
        flag = 0
        while dq:
            i, j = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r, c = i + dx, j + dy
                if -1 < r < N and -1 < c < N and not visit[r][c]:
                    if not board[r][c]: # 길 -> 지나가기
                        dq.append((r, c))
                        visit[r][c] = True
                        D[r][c] = D[i][j] + 1
                    else: # 물고기 발견
                        if dist and dist < D[i][j] + 1:
                            flag = 1
                            break
                        if board[r][c] == s: # 같은 사이즈 -> 지나가기
                            dq.append((r, c))
                            visit[r][c] = True
                            D[r][c] = D[i][j] + 1
                        else: # 다른 사이즈
                            if board[r][c] < s: # 작은 => 먹을 수 있음
                                dq.append((r, c))
                                visit[r][c] = True
                                D[r][c] = D[i][j] + 1
                                if not dist: # 유일하게 먹을 수 있는,
                                    dist = D[i][j] + 1
                                    ni, nj = r, c
                                elif dist == D[i][j] + 1: # 경쟁 물고기
                                    if i < ni: # 더 위에 있는 물고기
                                        ni, nj = r, c
                                    elif i == ni and j < nj: # 더 왼쪽 물고기
                                        ni, nj = r, c
            # print(D)
            if flag: break
        if initi == ni and initj == nj: # 물고기 잡아먹지 못함
            return t
        # 물고기 냠
        board[ni][nj] = 0
        i, j = ni, nj

        cnt += 1
        # print(board)
        t += dist
        if cnt == s:
            s += 1
            cnt = 0

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
f = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            f = 1
            break
    if f: break

result = bfs(i, j)
print(result)
