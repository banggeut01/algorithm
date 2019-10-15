# 17135.py 캐슬 디펜스

# die, set(),
# enemy, list([i, j])
import copy
def war(e):
    global ANS
    kill = 0
    while e:
        die = set()
        # 가장 가까운 위치 die에 넣기
        for x in range(len(s)):
            r, c = s[x][0], s[x][1] # 궁수 위치
            minD, dr, dc = 0, -1, -1
            for y in range(len(e)):
                i, j = e[y][0], e[y][1] # 적위치
                dist = abs(r - i) + abs(c - j)
                if dist <= D:
                    if minD == 0:
                        minD, dr, dc = dist, i, j
                    else:
                        if dist < minD:
                            minD, dr, dc = dist, i, j
                        elif dist == minD and j < dc:
                            minD, dr, dc = dist, i, j
            if dr != -1:
                die.add((dr, dc))
        kill += len(die)
        while die:
            i, j = die.pop()
            e.remove([i, j])
        x = 0
        while x < len(e):
            if e[x][0] + 1 != N:
                e[x][0] += 1
                x += 1
            else:
                e.pop(x)

    ANS = max(ANS, kill)
def getSet(k, sidx):
    if k == 3:
        tmp = copy.deepcopy(enemy)
        war(tmp)
        return
    for x in range(sidx, M):
        s.append((N, x))
        getSet(k + 1, x + 1)
        s.pop()

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
enemy = []
s = []
ecnt = 0
ANS = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            enemy.append([i, j])
            ecnt += 1
getSet(0, 0)
print(ANS)