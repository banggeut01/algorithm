# 2667.py 단지번호붙이기
from collections import deque
def bfs(i, j):
    cnt = 1 # 집 개수
    dq = deque()
    dq.append((i, j))
    board[i][j] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and board[nx][ny] == 1:
                dq.append((nx, ny))
                board[nx][ny] = 0
                cnt += 1
    return cnt

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
H = []
for i in range(N):
    for j in range(N):
        if board[i][j]:
            H.append(bfs(i, j))
H = sorted(H)
print(len(H))
for cnt in H:
    print(cnt)


