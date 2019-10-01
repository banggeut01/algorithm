# 7465.py 창용 마을 무리의 개수

def dfs(v):
    visit[v] = True
    for w in adj[v]:
        if not visit[w]:
            dfs(w)

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # N:사람, M:관계
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    visit = [False] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not visit[i]:
            ans += 1
            dfs(i)
    print('#{} {}'.format(tc, ans))
