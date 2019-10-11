# 17143.py 낚시왕

import collections
R, C, M = map(int, input().split()) # 행, 열, 상어수
board = [[0] * (C + 1) for _ in range(R + 1)]
# d 1:위, 2:아래, 3: 오른쪽, 4: 왼쪽
direct = {1: 2, 2: 1, 3: 4, 4: 3}
xy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
sh = [[0]] + [list(map(int, input().split())) for _ in range(M)]
# idx 상어번호, 0, 1: 좌표, 2: 속력, 3: 이동방향, 4: 크기
for x in range(1, M + 1):
    board[sh[x][0]][sh[x][1]] = x
visit = [False] * (M + 1)
result = 0
dq = collections.deque()
for j in range(1, C + 1):
    # 어부 위치 j
    for i in range(1, R + 1):
        if board[i][j]: # 상어 잡기
            n = board[i][j] # 상어번호
            board[i][j] = 0
            visit[n] = True
            result += sh[n][4]
            # print('#{}번'.format(n))
            break
    # 상어 이동
    for x in range(1, M + 1): # M마리 상어중 x상어
        if visit[x]: # 잡힌 상어
            continue
        initR, initC = sh[x][0], sh[x][1]
        dx, dy = xy[sh[x][3]][0], xy[sh[x][3]][1] # 이동 방향
        dist = sh[x][2]
        r, c = initR, initC
        dcnt = 0
        while dist > 0:
            nx, ny = r + dx, c + dy
            if 0 < nx < R + 1 and 0 < ny < C + 1:
                r, c = nx, ny
                dist -= 1
            else:
                dx, dy = dx * (-1), dy * (-1)
                dcnt += 1
        if dcnt % 2: # 방향이 바뀜
            sh[x][3] = direct[sh[x][3]]
        dq.append((x, r, c)) # 큐에 새로운 좌표 업데이트
        board[initR][initC] = 0
        sh[x][0], sh[x][1] = r, c
    while dq:
        x, r, c = dq.popleft()
        pos = board[r][c] #
        if pos: # 바꾸려는 자리에 상어가 있고
            if sh[pos][4] < sh[x][4]: # 크기 더 크면
                visit[pos] = True # 원래있던 상어 잡아먹힘
                board[r][c] = x
            else: # 새 상어 잡아먹힘
                visit[x] = True
        else:
            board[r][c] = x
print(result)





