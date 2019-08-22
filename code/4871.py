## 그래프 경로 4871.py
# 유향 그래프
# 재귀 DFS
import sys
sys.stdin = open('4871input.txt', 'r')


def DFS(v):
    visit[v] = True

    for w in matrix[v]:
        if not visit[w]:
            DFS(w)


t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split()) # 노드, 엣지
    matrix = [[] for _ in range(v + 1)]

    # 인접행렬
    for _ in range(e):
        start, end = map(int, input().split())
        matrix[start].append(end)

    s, g = map(int, input().split()) # 시작, 도착노드

    visit = [False] * (v + 1) # 방문 노드


    DFS(s)
    if visit[g]:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))