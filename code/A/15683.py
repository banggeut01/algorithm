# 15683.py 감시

import copy

def getZeroArea(chooList): 
    table = copy.deepcopy(board)
    for i, j, s, cNum in chooList: # cctv좌표ij, s:cctv타입, cNum:경우 번호
        for direct in cctv[s][cNum]:
            # direct:0-상, 1-우,..
            dx, dy = d[direct]
            row, col = i + dx, j + dy
            while -1 < row < N and -1 < col < M and table[row][col] != 6:
                if not table[row][col]:
                    table[row][col] = '#'
                row, col = row + dx, col + dy
    zcnt = 0
    for i in range(N):
        for j in range(M):
            if not table[i][j]:
                zcnt += 1
    del chooList
    del table
    return zcnt

def dfs(r, tmp):
    global result, cctvNum

    choose = copy.deepcopy(tmp)
    if len(choose) == cctvNum:
        zero = getZeroArea(choose)
        result = min(zero, result)
        return

    choose = copy.deepcopy(tmp)
    for i in range(r, N):
        for j in range(M):
            if not board[i][j]: continue
            if board[i][j] != 6 and board[i][j] != '#' and not used[i][j]: # cctv발견!
                s = board[i][j] # cctv 타입 1 ~ 5
                for cNum in range(len(cctv[s])): # 경우 선택 ex.s=1, len(cctv[s])=4 => case = 0, 1, 2, 3
                    choose.append((i, j, s, cNum))
                    used[i][j] = True
                    dfs(r, choose)
                    choose.pop()
                    used[i][j] = False
                return


N, M = map(int, input().split()) # N:행, M:열
board = [list(map(int, input().split())) for _ in range(N)]
# N, M = 6, 6
# board = [[0, 0, 0, 0, 0, 0],
#  [0, 2, 0, 0, 0, 0],
#  [0, 0, 0, 0, 6, 0],
#  [0, 6, 0, 0, 2, 0],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 5]]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # [0]:상, [1]:우, [2]:하, [3]:좌
cctv = [[],  # [0]
        [[0], [1], [2], [3]],  # [1] 4가지
        [[0, 2], [1, 3]],  # [2] 2가지
        [[0, 1], [1, 2], [2, 3], [3, 0]],  # [3] 4가지
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # [4] 4가지
        [[0, 1, 2, 3]]]  # [5] 1가지
cctvNum, result = 0, N * M
zero = 0
used = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            zero += 1
            continue
        if board[i][j] != 6: cctvNum += 1
dfs(0, []) # 시작행, 선택된 cctv 정보
print(result)

