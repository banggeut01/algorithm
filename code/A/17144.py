# 17144.py 미세먼지안녕

def spreadDust(): #확산
    for i in range(R):
        for j in range(C):
            move[i][j] = dust[i][j] // 5

    for i in range(R):
        for j in range(C):
            if dust[i][j] != -1:
                for idx in range(4):  # 4 방향에 대해
                    r, c = i + x[idx], j + y[idx]
                    if 0 <= r < R and 0 <= c < C and dust[r][c] != -1:
                        dust[i][j] -= move[i][j]
                        dust[i][j] += move[r][c]

def cleanAir(start, dir): # 시작행, dir-방향 -1:위, 1:아래
    if dir == -1:
        # 1. 위로
        for i in range(start - 1, 0, -1):
            dust[i][0]= dust[i - 1][0]
        # 2. 오른쪽으로
        for j in range(0, C - 1):
            dust[0][j] = dust[0][j + 1]
        # 3. 아래로
        for i in range(0, start):
            dust[i][C - 1] = dust[i + 1][C - 1]
        # 4. 왼쪽으로
        for j in range(C - 1, 1, -1):
            dust[start][j] = dust[start][j - 1]
    else:
        for i in range(start + 1, R - 1):
            dust[i][0] = dust[i + 1][0]
        for j in range(0, C - 1):
            dust[R - 1][j] = dust[R - 1][j + 1]
        for i in range(R - 1, start, -1):
            dust[i][C - 1] = dust[i - 1][C - 1]
        for j in range(C - 1, 1, -1):
            dust[start][j] = dust[start][j - 1]
    dust[start][1] = 0

R, C, T = map(int, input().split()) # R:행, C:열, T:초
dust = [list(map(int, input().split())) for _ in range(R)]
move = [[0] * C for _ in range(R)]
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
cleaner = [] # 공기청정기
for i in range(R):
    if dust[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i + 1)
        break
# T초 동안
for _ in range(T):
    spreadDust()
    cleanAir(cleaner[0], -1) # 반시계방향
    cleanAir(cleaner[1], 1) # 시계방향

dust[cleaner[0]][0], dust[cleaner[1]][0] = 0, 0
totalDust = 0
for i in range(R):
    for j in range(C):
        totalDust += dust[i][j]
print(totalDust)
import pprint
pprint.pprint(dust)