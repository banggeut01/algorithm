# 5249. 최소 신장 트리

t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    edge = []
    # adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge.append((w, n1, n2))
    edge = sorted(edge)
    visit = [False] * (V + 1)
    total = 0
    choosed = 0
    print(edge)
    adj = [[] for _ in range(V + 1)]
    for x in range(len(edge)):
        w, n1, n2 = edge[x]
        if not visit[n1] or not visit[n2]: # 선택
            total += w
            visit[n1] = True
            visit[n2] = True
            choosed += 1
            adj[n1].append(n2)
            adj[n2].append(n1)
            if dfs(n1):

            print(w)
        if choosed == V + 1:
            break
    print('#{} {}'.format(tc, total))
