# 5643.py 키 순서

# 정방향 순회 노드 개수 + 역방향 순회 노드 개수 = > 전체 - 1(자신)
from collections import deque
def bfs(s, visit, adj):
    visit[s] = True
    dq = deque()
    dq.append(s)
    cnt = 0
    while dq:
        n = dq.pop()
        for w in adj[n]:
            if not visit[w]:
                visit[w] = True
                cnt += 1
                dq.append(w)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 학생 수
    M = int(input()) # 키 리스트 개수
    adj1 = [[] for _ in range(N + 1)] # 정방향
    adj2 = [[] for _ in range(N + 1)] # 역방향
    result = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj1[n1].append(n2)
        adj2[n2].append(n1)
    for s in range(1, N + 1):
        visit1 = [False] * (N + 1)
        visit2 = [False] * (N + 1)
        cnt1 = bfs(s, visit1, adj1)
        cnt2 = bfs(s, visit2, adj2)
        if cnt1 + cnt2 == N - 1:
            result += 1
    print('#{} {}'.format(tc, result))