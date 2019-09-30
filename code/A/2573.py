# 2573.py 빙산
import collections
def bfs(i, j):
    dq = collections.deque()
    visit[i][j] = True
    dq.append((i, j))
    while dq:
        i, j = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < M:
                if not board[r][c]:
                    melt[i][j] += 1
                elif not visit[r][c]:
                    dq.append((r, c))
                    visit[r][c] = True

def updateBoard(): ##### 고칠 곳만 고칠 수 있도록
    for i in range(N):
        for j in range(M):
            d = board[i][j] - melt[i][j]
            if d <= 0:
                board[i][j] = 0
            else:
                board[i][j] = d

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    flag = 0
    visit = [[False] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                if not flag:
                    flag = 1
                    bfs(i, j)
                else: # 빙산 2개 이상
                    flag = 2
                    break
        if flag == 2:
            break
    if flag == 2:
        break
    updateBoard()
    ans += 1
print(ans)