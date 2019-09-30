# 14889.py 스타크와 링크

def getPower(g):
    power = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            power = power + board[g[i]][g[j]] + board[g[j]][g[i]]
    return power

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MIN = N * (N - 1) * 100
M = N // 2
for i in range(1 << N):
    g1, g2 = [], []
    for j in range(N):
        if i & (1 << j):
            g1.append(j)
        else:
            g2.append(j)
    if len(g1) == M:
        dist = abs(getPower(g1) - getPower(g2))
        MIN = min(dist, MIN)
print(MIN)