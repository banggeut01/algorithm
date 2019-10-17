# 5521.py 상원이의 생일파티
from collections import deque
def bfs():
    dq = deque()
    dq.append(1)
    visit[1] = True
    total = 0
    while dq:
        v = dq.popleft()
        for w in adj[v]:
            if not visit[w]:
                visit[w] = True
                if D[v] + 1 <= 2:
                    dq.append(w)
                    D[w] = D[v] + 1
                    total += 1
    return total

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    # 1번노드:상원
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    visit = [False] * (N + 1)
    D = [0] * (N + 1)
    result = bfs()
    print('#{} {}'.format(tc, result))