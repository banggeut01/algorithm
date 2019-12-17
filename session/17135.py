# 17135.py 캐슬 디펜스
from copy import deepcopy
def updateMAX(E): # 한 궁수 조합에 대해 적 수 구함
    global MAX
    cnt = 0
    while E:
        # 제거할 적 고름(최소 거리)
        remList = set()
        for ay in A:
            dist, remx, remy, flag = 30, 15, 15, False
            for ex, ey in E:
                tmp = abs(N - ex) + abs(ay - ey)
                if tmp > D:
                    continue
                if tmp < dist or (tmp == dist and ey < remy):
                    dist, remx, remy, flag = tmp, ex, ey, True
            if flag:
                remList.add((remx, remy))
        # 적 제거
        cnt += len(remList)
        for ex, ey in remList:
            E.remove((ex, ey))
        # 적 이동
        i = 0
        while i < len(E):
            ex, ey = E[i]
            if ex + 1 < N:
                E[i] = (ex + 1, ey)
                i += 1
            else: E.pop(i)
    MAX = max(MAX, cnt)
    return

def back(k, s):
    if k == 3:
        copied = deepcopy(enemy)
        updateMAX(copied)
        return

    for idx in range(s, M):
        A[k] = idx
        back(k + 1, idx + 1)

N, M, D = map(int, input().split()) # 행,열,거리제한
board = [list(map(int, input().split())) for _ in range(N)]
enemy = [] # 적
for i in range(N - 1, -1, -1):
    for j in range(M):
        if board[i][j]:
            enemy.append((i, j))
A = [-1] * 3  # 궁수 3명 열 좌표
MAX = 0
back(0, 0)
print(MAX)