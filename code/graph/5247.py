# 5247.py 연산
from collections import deque

def bfs(N):
    dq = deque()
    dq.append(N)
    visit[N] = True
    x = [1, -1, -10]
    while dq:
        cur = dq.popleft()
        tmp = cur * 2
        if tmp <= 1000000:
            if not visit[tmp]:
                if tmp == M:
                    return D[cur] + 1
                dq.append(tmp)
                visit[tmp] = True
                D[tmp] = D[cur] + 1
        for i in range(3):
            tmp = cur + x[i]
            if tmp > 1000000: continue
            if not visit[tmp]:
                if tmp == M:
                    return D[cur] + 1
                dq.append(tmp)
                visit[tmp] = True
                D[tmp] = D[cur] + 1

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # N -> M 몇번 연산?
    visit = [False] * 1000001
    D = [0] * 1000001
    result = bfs(N)
    print('#{} {}'.format(tc, result))
