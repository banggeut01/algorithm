# 4012_2.py 요리사
# 부분집합
import sys
sys.stdin = open('4012input.txt', 'r')

def getSynergy(choosed):
    tmp = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            tmp = tmp + ingrd[choosed[i]][choosed[j]] + ingrd[choosed[j]][choosed[i]]
    return tmp

def getSet():
    global MIN
    for i in range(1 << N):
        g1, g2 = [], []  # 식재료 조합
        for j in range(N):
            if i & (1 << j):
                g1.append(j)
            else:
                g2.append(j)
        if len(g1) == M:
            dist = abs(getSynergy(g1) - getSynergy(g2))
            MIN = min(MIN, dist)

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    ingrd = [list(map(int, input().split())) for _ in range(N)]
    MIN = 20000 * N * N
    M = N // 2
    getSet()
    print('#{} {}'.format(tc, MIN))
    