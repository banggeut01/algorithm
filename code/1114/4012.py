# 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open('4012input.txt', 'r')
def getSng(g):
    rtn = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            rtn += (board[g[i]][g[j]] + board[g[j]][g[i]])
    return rtn

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MIN = 0xffffff
    for i in range(1 << N):
        g1, g2 = [], []
        for j in range(N):
            if i & 1 << j: g1.append(j)
            else: g2.append(j)
        if len(g1) == N // 2:
            sng1 = getSng(g1)
            sng2 = getSng(g2)
            MIN = min(MIN, abs(sng1 - sng2))
    print('#{} {}'.format(tc, MIN))