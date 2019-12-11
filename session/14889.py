# 14889.py 스타트와 링크
def getSynergy(g):
    total = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            total += (board[g[i]][g[j]] + board[g[j]][g[i]])
    return total

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MIN = 0xffffff
for i in range(1 << N):
    g1, g2 = [], []
    for j in range(N):
        if i & 1 << j: g1.append(j)
        else: g2.append(j)
    if len(g1) == N // 2:
        s1 = getSynergy(g1)
        s2 = getSynergy(g2)
        MIN = min(MIN, abs(s1 - s2))
print(MIN)