# 1953. [모의 SW 역량테스트] 탈주범 검거
import sys
sys.stdin = open('1953input.txt', 'r')

from collections import deque
def bfs(r, c):
    dq = deque()
    visit = [[False] * M for _ in range(N)]
    visit[r][c] = True
    dq.append((r, c, 1))
    cnt = 0
    while dq:
        x, y, t = dq.popleft() # 행, 열, 시간
        if t > L: return cnt
        cnt += 1
        dir = board[x][y]
        for dx, dy in d[dir]:
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not visit[nx][ny] and board[nx][ny]:
                if not (dx * (-1), dy * (-1)) in d[board[nx][ny]]: continue
                visit[nx][ny] = True
                dq.append((nx, ny, t + 1))
    return cnt

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split()) # N:세로,M:가로,RC:맨홀뚜껑,L시간
    board = [list(map(int, input().split())) for _ in range(N)]
    d = [[0],
         [(-1, 0), (1, 0), (0, -1), (0, 1)],    # [1] 상하좌우
         [(-1, 0), (1, 0)],                     # [2] 상 하
         [(0, -1), (0, 1)],                     # [3] 좌 우
         [(-1, 0), (0, 1)],                     # [4] 상, 우
         [(1, 0), (0, 1)],                      # [5] 하, 우
         [(1, 0), (0, -1)],                     # [6] 하, 좌
         [(-1, 0), (0, -1)]]                    # [7] 상, 좌
    result = bfs(R, C)
    print('#{} {}'.format(tc, result))