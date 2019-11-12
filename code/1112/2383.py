# 2383.py [모의 SW 역량테스트] 점심 식사시간
import sys
sys.stdin = open('2383input.txt', 'r')

def getTime(t, l): # t: 사람-입구 거리 배열, l: 계단길이
    for idx in range(len(t)):
        if idx < 3:
            t[idx] += l
        else:
            if t[idx - 3] > t[idx]:
                t[idx] = t[idx - 3] + l
            else:
                t[idx] += l
    if t: return t[-1]
    else: return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    P, S = [], [] # P: 사람 좌표(x, y), S: 계단좌표&길이(x, y, len)
    MIN = 0xffffff
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                P.append((i, j))
            elif board[i][j] > 1:
                S.append((i, j, board[i][j]))
    dct = [dict() for _ in range(2)]
    for x in range(len(S)): # 한 계단에 대해
        sr, sc, tmp = S[x]
        for y in range(len(P)): # 사람-계단 거리를 구함
            pr, pc = P[y]
            d = abs(sr - pr) + abs(sc - pc)
            dct[x][(pr, pc)] = d
    for i in range(1 << len(P)):
        time0, time1 = [], []
        for j in range(len(P)):
            if i & 1 << j:
                time0.append(dct[0][P[j]] + 1)
            else:
                time1.append(dct[1][P[j]] + 1)
        time0 = sorted(time0)
        time1 = sorted(time1)
        t0 = getTime(time0, S[0][2])
        t1 = getTime(time1, S[1][2])
        MIN = min(MIN, max(t0, t1))
    print('#{} {}'.format(tc, MIN))
