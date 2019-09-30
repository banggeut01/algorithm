# 16234.py 인구 이동
import collections
def bfs(i, j):
    tmp = []
    dq = collections.deque()
    visit[i][j] = True
    dq.append((i, j))
    tmp.append((i, j))
    total = board[i][j]
    while dq:
        i, j = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < N and not visit[r][c] \
                    and L <= abs(board[i][j] - board[r][c]) <= R:
                tmp.append((r, c))
                visit[r][c] = True
                dq.append((r, c))
                total += board[r][c]
    if len(tmp) == 1:
        return False
    else:
        M = len(tmp)
        for i in range(M):
            r, c = tmp[i]
            board[r][c] = total // M
        return True


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    flag = False
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bfs(i, j):
                    if not flag:
                        ans += 1
                    flag = True
    if not flag:
        break
print(ans)