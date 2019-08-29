# 5102.py 노드의 거리
# 무방향
# BFS

import collections
import sys
sys.stdin = open('5102input.txt', 'r')

def bfs():
    visit = [False] * (V + 1)
    visit[S] = True
    dq = collections.deque()
    dq.append(S)

    while dq:
        node = dq.popleft()
        for n in adj[node]:
            if n == G: # 경로 끝!
                return D[node] + 1
            if not visit[n]: # 방문안했으면,
                visit[n] = True
                dq.append(n)
                D[n] = D[node] + 1

    return 0

t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)] # 인접리스트
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    S, G = map(int, input().split())
    D = [0] * (V + 1)
    result = bfs()
    print('#{} {}'.format(tc, result))