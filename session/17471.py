# 17471.py 게리맨더링
from collections import deque
def bfs(g, cnt):
    visit = [False] * (N + 1)
    dq = deque()
    dq.append(g[0])
    visit[g[0]] = True
    total, cnt = P[g[0]], 1 # 인구수, 인접구역수
    while dq:
        v = dq.popleft()
        for w in adj[v]:
            if not visit[w] and w in g:
                visit[w] = True
                dq.append(w)
                total, cnt = total + P[w], cnt + 1
    return total, cnt

def getSet(k, acnt, bcnt):
    if k > N:
        if acnt and bcnt:
            p1, ac = bfs(A, acnt)
            p2, bc = bfs(B, bcnt)
            if ac + bc == N:
                global MIN
                if MIN == -1: MIN = abs(p1 - p2)
                else: MIN = min(MIN, abs(p1 - p2))
        return

    A.append(k)
    getSet(k + 1, acnt + 1, bcnt)
    A.pop()
    B.append(k)
    getSet(k + 1, acnt, bcnt + 1)
    B.pop()

N = int(input())
P = [0] + list(map(int, input().split())) # 인구
adj = [[] for _ in range(N + 1)]
for s in range(1, N + 1):
    li = list(map(int, input().split()))
    for x in range(1, li[0] + 1):
        adj[s].append(li[x])
A, B = [], []
MIN = -1
getSet(1, 0, 0)
print(MIN)