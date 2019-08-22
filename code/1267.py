# 작업순서 1267.py
# DFS
# 유향 그래프

import sys
sys.stdin = open('1267input.txt', 'r')


def DFS(v):
    visit[v] == True
    result.append(v)

    for w in adj[v]:
        if not visit[w]:
            DFS(w)



for tc in range(1, 11):
    v, e = map(int, input().split())
    node = list(map(int, input().split()))

    adj = [[] for _ in range(v + 1)] # 인접 리스트
    result = [] # 답
    comein = [0] * (v + 1)

    for i in range(e):
        adj[node[2 * i]].append(node[2 * i + 1])
        comein[node[2 * i + 1]] += 1
    print(adj)
    print(comein)
    visit = [False] * (v + 1)

    # 루트노트 찾기
    for i in range(1, v + 1):
        if not comein[i] and adj[i]: # 들어오는 간선 없고, 나가는 간선 있는 경우
            start = i
            break

    DFS(start)
    result = list(map(str, result))
    print('#{} {}'.format(tc, ' '.join(result)))

