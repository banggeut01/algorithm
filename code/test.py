import collections



def bfs(i,j):  # 시작점
    queue = collections.deque()  # 큐생성
    visit[i][j] = True  # 방문 표시
    queue.append((i, j))  # 큐에 삽입

    while queue:  # 빈큐 아닐동안
        i, j = queue.popleft() # 큐에서 하나 꺼내옴
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r, c = i + dx, j + dy
            if -1 < r < N and -1 < c < M and not visit[r][c] and not board[r][c]:
                visit[r][c] = True
                queue.append((r, c))
                D[r][c] = D[i][j] + 1

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
D = [[0] * M for _ in range(N)]
# g에 input 삽입하기
bfs(1, 1)
import pprint
pprint.pprint(D)