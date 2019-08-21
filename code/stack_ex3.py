# stack_ex3.py

import sys; sys.stdin = open('DFS_input.txt', 'r')


def DFS(v): # v = 현재 방문하는 정점

    visit[v] = True; print(v, end='')

    for w in g[v]:
        if not visit[w]: # v에 방문하지 않은 인접정점 w를 찾아서
            DFS(w)


v, e = map(int, input().split()) # 정점수, 간선수
g = [[] for _ in range(v + 1)]   # 1 ~ v 까지
visit = [False] * (v + 1)        # 방문 정보

for _ in range(e):
    u, v = map(int, input().split()) # 정점1, 정점2
    g[u].append(v)
    g[v].append(u) # 무향 그래프

print(g)

DFS(1)