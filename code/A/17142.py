# 17142.py 연구소 3

# 0: 빈칸, 1: 벽, 2: 바이러스
# 바이러스 M개를 활성상태로 변경하려고 함
# 활성이 비활성 위치로 가면 비활성 ==> 활성으로 변함
# -: 벽, *: 비활성, 활성: 0, 빈칸은 바이러스가 퍼지는 시간!
# 모든 빈칸에 바이러스 퍼뜨리는 최소 시간을 구하여라.
# 바이러스 중 M개를 고른다. => 집합 (원소 개수 10개 이하)
import collections
def bfs():
    global result
    changedCnt = 0
    maxCnt = 0
    D = [[0] * N for _ in range(N)]
    while dq:
        i, j = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r, c  = i + dx, j + dy
            if -1 < r < N and -1 < c < N and not visit[r][c] and (r, c) not in act:
                if not board[r][c]:
                    dq.append((r, c))
                    visit[r][c] = True
                    D[r][c] = D[i][j] + 1
                    maxCnt = max(maxCnt, D[r][c])
                    changedCnt += 1
                elif board[r][c] == '*': # 빈칸 or 비활성 => 활성
                    dq.append((r, c))
                    visit[r][c] = True
                    D[r][c] = D[i][j] + 1
    if emptyCnt != changedCnt: # 빈칸 + 비활성 개수 = 상태변화 개수
        return

    if result == -1:
        result = maxCnt
    else:
        result = min(maxCnt, result)

N, M = map(int, input().split()) # N: 행열크기, M: 선택한 바이러스 개수
board = [list(map(int, input().split())) for _ in range(N)]
result = -1 # 답
virus = []
emptyCnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
        elif not board[i][j]:
            emptyCnt += 1
V = len(virus)
if not emptyCnt:
    result = 0
else:
    # 부분 집합
    for i in range(1 << V):
        act, inact = [], []
        for j in range(V):
            if i & (1 << j):
                act.append(virus[j])
            else:
                inact.append(virus[j])
        if len(act) == M:
            for x, y in inact:
                board[x][y] = '*'
            dq = collections.deque()
            visit = [[0] * N for _ in range(N)]
            for x, y in act:
                visit[x][y] = True
                dq.append((x, y))
            bfs()
            for x, y in inact:
                board[x][y] = 2
print(result)


