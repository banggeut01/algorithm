# 14500.py 테트로미노

def back(x, y, k, total):
    if k == 4:
        global MAX
        MAX = max(MAX, total)
        return
    # ㅗ 모양
    if k == 2:
        tmp = []
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not visit[nx][ny]:
                tmp.append((nx, ny))
        if tmp:
            for i in range(1 << len(tmp)):
                setLi = []
                for j in range(len(tmp)):
                   if i & 1 << j:
                       setLi.append(tmp[j])
                if len(setLi) == 1:
                    nx, ny = setLi.pop()
                    visit[nx][ny] = True
                    back(nx, ny, k + 1, total + board[nx][ny])
                    visit[nx][ny] = False
                elif len(setLi) == 2:
                    nx1, ny1 = setLi.pop()
                    nx2, ny2 = setLi.pop()
                    visit[nx1][ny1] = True
                    visit[nx2][ny2] = True
                    back(nx1, ny1, k + 2, total + board[nx1][ny1] + board[nx2][ny2])
                    back(nx2, ny2, k + 2, total + board[nx1][ny1] + board[nx2][ny2])
                    visit[nx1][ny1] = False
                    visit[nx2][ny2] = False
    else:
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not visit[nx][ny]:
                visit[nx][ny] = True
                back(nx, ny, k + 1, total + board[nx][ny])
                visit[nx][ny] = False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
MAX = 0
for i in range(N):
    for j in range(M):
        back(i, j, 0, 0)
print(MAX)