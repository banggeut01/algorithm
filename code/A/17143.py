# 17143.py 낚시왕


R, C, M = map(int, input().split()) # 행, 열, 상어수
board = [[0] * (C + 1) for _ in range(R + 1)]
pos, s, d, z = [], [], [], [] # idx는 상어 번호
# d 1:위, 2:아래, 3: 오른쪽, 4: 왼쪽
direct = {1: 2, 2: 1, 3: 4, 4: 3}
xy = [(0, 0), (-1, 0), (1, 0), (1, 0), (-1, 0)]
for idx in range(M):
    tmp = list(map(int, input().split()))
    pos.append([tmp[0], tmp[1]]) # 위치
    board[pos[0][0]][pos[0][1]] = idx
    s.append(tmp[2]) # 속력
    d.append(tmp[3]) # 방향
    z.append(tmp[4]) # 크기
result = 0
for j in range(1, C + 1):
    # 어부 위치 j
    for i in range(1, R + 1):
        if board[i][j]: # 상어 잡기
            n = board[i][j]
            result += z[n]
            pos.pop(n)
            s.pop(n)
            d.pop(n)
            z.pop(n)
            break
    # 상어 이동
    for x in range(len(pos)): # x 상어 한마리
        initR, initC = pos[x][0], pos[x][1]
        dx, dy = xy[d[x]][0], xy[d[x]][1]
        dist = s[x]
        r, c = initR, initC
        dcnt = 0
        while dist > 0:
            nx, ny = r + dx, c + dy
            if 0 < nx < R and 0 < ny < C:
                r, c = nx, ny
                dist -= 1
            else:
                dx, dy = dx * (-1), dy * (-1)
                dcnt += 1
        if dcnt % 2: # 방향이 바뀜
            oriPos = board[initR][initC]
            print(d)
            print(oriPos)
            print(d[oriPos])
            d[oriPos] = direct[d[oriPos]]
        if board[r][c] and z[board[r][c]] < z[board[initR][initC]]: # 잡아먹기
            # 바꾸고
            origin, target = board[initR][initC], board[r][c]
            pos[origin][0], pos[target][0] = pos[target][0], pos[origin][0]
            pos[origin][1], pos[target][1] = pos[target][1], pos[origin][1]
            s[origin], s[target] = s[target], s[origin]
            d[origin], d[target] = d[target], d[origin]
            z[origin], z[target] = z[target], z[origin]
            # pop
            pos.pop(origin)
            s.pop(origin)
            d.pop(origin)
            z.pop(origin)
print(result)





