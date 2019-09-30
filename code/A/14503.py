# 14503.py 로봇 청소기

def dfs(i, j, d):
    cnt = 1
    while True:
        newd = d
        for _ in range(4): # 북 > 서 > 남 > 동
            newd = dlist[newd - 1] # 현재 위치에서 왼쪽 방향
            dx, dy = xy[newd]
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < M and not visit[r][c] and not board[r][c]: # 아직 청소 안됨
                visit[r][c] = True
                i, j, d, cnt = r, c, newd, cnt + 1 # 전진
                break
        else: # 네방향 갈 곳 없음
            newd = dlist[d - 2] # 후진 방향
            dx, dy = xy[newd]
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < M and not board[r][c]:
                i, j = r, c # 후진
            else:
                return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d 방향 - 0:북, 1:동, 2:남, 3:서
board = [list(map(int, input().split())) for _ in range(N)]
dlist = [0, 1, 2, 3]
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # xy[0]: 북쪽으로 한칸 전진
visit = [[False] * M for _ in range(N)]
visit[r][c] = True
result = dfs(r, c, d)
print(result)