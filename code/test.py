
from collections import deque
def BFS(s):
    D = [0xffffff] * (V + 1) # D[] 초기값 설정
    Q = deque()
    Q.append(s); D[s] = 0

    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u]: # u ----> v
                D[v] += D[u] + w
                Q.append(v)

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

