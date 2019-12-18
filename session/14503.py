# 14503.py 로봇청소기
def getCnt(x, y, d):
    visit = [[False] * M for _ in range(N)]
    ret = 1
    visit[x][y] = True
    while True:
        for _ in range(4):
            dx, dy = xy[dir[d]] # 왼쪽 방향
            nx, ny = x + dx, y + dy
            if not board[nx][ny] and not visit[nx][ny]: # 2-a
                d = dir[d]
                x, y = nx, ny
                ret += 1 # 1. 청소
                visit[x][y] = True
                break
            else: # 2-b
                d = dir[d]
        else: # 2-c,d
            op = d #  반대방향
            for _ in range(2):
                op = dir[op]
            nx, ny = x + xy[op][0], y + xy[op][1]
            if not board[nx][ny]: x, y = nx, ny # 2-c
            else: break # 2-d
    return ret

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d:방향 - 0북, 1동, 2남, 3서
board = [list(map(int, input().split())) for _ in range(N)]
dir = { 0: 3, 3: 2, 2: 1, 1: 0 }
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(getCnt(r, c, d))
