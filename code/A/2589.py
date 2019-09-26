# 2589.py 보물섬

import collections

def bfs(x, y):
    global MAX
    visit = [[False] * M for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    dq = collections.deque()
    dq.append((x, y))
    while dq:
        i, j = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < M and board[r][c] == 'L' and not visit[r][c]:
                visit[r][c] = True
                dq.append((r, c))
                D[r][c] = D[i][j] + 1
                MAX = max(MAX, D[r][c])



N, M = map(int, input().split()) # 행, 열
board = [input() for _ in range(N)]

# N, M = 5, 7
#
# board = ['WLLWWWL',
# 'LLLWLLL',
# 'LWLWLWW',
# 'LWLWLLL',
# 'WLLWLWW']

MAX = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            bfs(i, j)
print(MAX)