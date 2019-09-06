# 17070.py 파이프 옮기기 1

def dfs(i, j, s): # 현재 좌표ij, s:상태
    global cnt

    if i == N - 1 and j == N - 1: # 도착
        cnt += 1
        return

    for dx, dy in d[s]:
        r, c = i + dx, j + dy
        if -1 < r < N and -1 < c < N and not board[r][c]: # 갈 수 있으면,
            if dx == dy: # 대각선 - 오른쪽, 아래도 확인해야
                # '-1 < r - 1 < N and -1 < c - 1 < N' 조건 생략 가능, i, j, r, c가 범위내 있기 때문
                if not board[r - 1][c] and not board[r][c - 1]:
                    s = 2
                else: # 못감
                    continue
            elif dy == 1: s = 0     # 가로
            else: s = 1             # 세로
            dfs(r, c, s) # 가기

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
state = 0 # 0:가로, 1:세로, 2:대각선
d = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]]
cnt = 0
if not board[N - 1][N - 1]:
    dfs(0, 1, 0) # 시작점0,1 / state:0가로
print(cnt)