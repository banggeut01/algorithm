# stack_ex3-1.py

import sys; sys.stdin = open('DFS_input.txt', 'r')


def DFS(v):
    # 시작점을 방문하고 스택에 push
    stack = [] # 방문 경로 저장할 스택
    visit[v] = True; print(v, end='')
    stack.append(v)
    while stack: # 빈 스택이 아닐동안 반복
        for w in g[v]:
            if not visit[w]: # v에 방문하지 않은 인접정점 w를 찾아서
                visit[w] = True; print(w, end='')
                stack.append(w) # w를 방문하고, v를 스택에 push
                v = w # v를 w로 설정
                break
        else: # 인접정점이 없다면, 스택에서 pop()해서
            v = stack.pop() # v로 설정


v, e = map(int, input().split()) # 정점수, 간선수
g = [[] for _ in range(v + 1)]   # 1 ~ v 까지
visit = [False] * (v + 1)        # 방문 정보

for _ in range(e):
    u, v = map(int, input().split()) # 정점1, 정점2
    g[u].append(v)
    g[v].append(u) # 무향 그래프

print(g)

DFS(1)