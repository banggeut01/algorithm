# 5248.py 그룹 나누기
def dfs(v):
    visit[v] = True
    for w in adj[v]:
        if not visit[w]:
            visit[w] = True
            dfs(w)

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # 노드(1-N), 간선
    adj = [[] for _ in range(N + 1)]
    li = list(map(int, input().split()))
    for x in range(len(li) // 2):
        v1, v2 = li[x * 2], li[x * 2 + 1]
        adj[v1].append(v2)
        adj[v2].append(v1)
    visit = [False] * (N + 1)
    cnt = 0
    for v in range(1, N + 1):
        if not visit[v]:
            dfs(v)
            cnt += 1
    print('#{} {}'.format(tc, cnt))