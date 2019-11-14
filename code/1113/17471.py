# 17471.py 게리맨더링
# 두 개의 선거구로 나누고 선거구 총 인구수 차이 최솟값 출력
# 두 선거구로 나눌 수 없는 경우 -1
from collections import deque
def getTotal(g1):
    dq = deque()
    dq.append(g1[0])
    visit = [False] * (N + 1)
    visit[g1[0]] = True
    cnt, total = 0, 0 # cnt:인접 선거구 구역 수, total:전체 인구수
    while dq:
        v = dq.popleft()
        cnt += 1
        total += P[v]
        for w in adj[v]:
            if not visit[w] and w in g1:
                visit[w] = True
                dq.append(w)
    return total, cnt

N = int(input()) # 구역 개수
P = [0] + list(map(int, input().split())) # 1 ~ N번 구역당 인구수
adj = [[] for _ in range(N + 1)]
MIN = -1 # 답
for s in range(1, N + 1): # s: 노드1
    li = list(map(int, input().split()))
    for e in range(1, li[0] + 1): # li[e]: 노드2
        adj[s].append(li[e])
# 선거구 나누기 N개의 원소 2개의 부분집합으로
for i in range(1, 1 << (N + 1)):
    g1, g2 = [], []
    for j in range(1, N + 1):
        if i & 1 << j: g1.append(j)
        else: g2.append(j)
    if g1 and g2: # 두 선거구가 1개 이상의 구역일 때,
        p1, adjNum1 = getTotal(g1)
        p2, adjNum2 = getTotal(g2)
        if adjNum1 + adjNum2 == N: # 각 구역 인접 구역이 전체N선거구 구역일 때
            if MIN == -1: MIN = abs(p1 - p2)
            else: MIN = min(MIN, abs(p1 - p2))
print(MIN)

