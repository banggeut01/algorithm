# 2468.py 안전영역
import sys
sys.setrecursionlimit(10000)

def dfs(i, j, h):
    visit[i][j] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        r, c = i + dx, j + dy
        if -1 < r < N and -1 < c < N and board[r][c] > h and not visit[r][c]:
            dfs(r, c, h)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAXH, ANS = 0, 1 # ANS:1 -> 아무 지역도 잠기지 않음
for i in range(N):
    MAXH = max(MAXH, max(board[i]))
for h in range(1, MAXH): # 1 ~ MAXH-1
    cnt = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visit[i][j]:
                dfs(i, j, h)
                cnt += 1
    ANS = max(ANS, cnt)
print(ANS)
