# 1868.py 파핑파핑 지뢰찾기
from collections import deque
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visit[x][y] = True
    cnt = 1 # 체크된 영역 개수
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), \
                              (0, 1), (1, -1), (1, 0), (1, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
                visit[nx][ny] = True
                cnt += 1
                if not mine[nx][ny]: # 0 아닌 숫자일 때
                    dq.append((nx, ny))
    return cnt

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    mine = [[0] * N for _ in range(N)] # 인접8방향에 대한 지뢰개수 저장
    for x in range(N):
        for y in range(N):
            if board[x][y] == '*':
                mine[x][y] = -1
                for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), \
                              (0, 1), (1, -1), (1, 0), (1, 1):
                    nx, ny = x + dx, y + dy
                    if -1 < nx < N and -1 < ny < N and board[nx][ny] != '*':
                        mine[nx][ny] += 1

    visit = [[False] * N for _ in range(N)]
    ANS = 0 # 클릭 수
    checkedCnt = 0 # 체크된 영역 개수
    # 0인 지점부터 체크
    for x in range(N):
        for y in range(N):
            if not mine[x][y] and not visit[x][y]:
                ANS += 1
                checkedCnt += bfs(x, y)
    # 1이상 지점 체크
    for x in range(N):
        for y in range(N):
            if mine[x][y] > 0 and not visit[x][y]:
                ANS += 1
    print('#{} {}'.format(tc, ANS))
