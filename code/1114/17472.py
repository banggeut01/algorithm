# 17472 다리 만들기2
import pprint
from collections import deque
def dfs(x, y):
    board[x][y] = islandCnt
    visit[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and board[nx][ny] and not visit[nx][ny]:
            dfs(nx, ny)

def makeBridge(i, j): # 다리를 만듬
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        cnt = 0
        x, y = i + dx, j + dy
        while -1 < x < N and -1 < y < M and not board[x][y]:
            cnt += 1
            x, y = x + dx, y + dy
        if -1 < x < N and -1 < y < M and board[x][y]:
            if cnt < 2: continue
            s, e = min(board[i][j], board[x][y]), max(board[i][j], board[x][y])
            if dist.get((s, e)): dist[(s, e)] = min(dist[(s, e)], cnt)
            else: dist[(s, e)] = cnt

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def getMIN():
    cnt, total = 0, 0
    for d, s, e in bridges:
        p1 = find_set(s)
        p2 = find_set(e)
        if p1 != p2:
            cnt += 1
            total += d
        if cnt == islandCnt - 1:
            return total
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
islandCnt = 0 # 섬 개수
dist = dict()
visit = [[False] * M for _ in range(N)]

# 섬마다 다른 번호 부여하기
for i in range(N):
    for j in range(M):
        if board[i][j] and not visit[i][j]:
            islandCnt += 1
            dfs(i, j)
p = [x for x in range(islandCnt + 1)]
# 다리 만들기
for i in range(N):
    for j in range(M):
        if board[i][j]:
            makeBridge(i, j)

bridges = []
for key, d in dist.items():
    s, e = key
    bridges.append((d, s, e))
bridges = sorted(bridges)
# pprint.pprint(board)
# print(bridges)

print(getMIN())