# 14891.py 톱니바퀴
from collections import deque
def dfs(x, d): # x:톱니번호 1-4, d: 방향 -1, 1
    visit[x] = True
    l, r = G[x][6], G[x][2]
    if d == -1: # 반시계
        # tmp = G[x].popleft()
        # G[x].append(tmp)
        G[x].append(G[x].popleft())
    else: # 시계
        # tmp = G[x].popleft()
        # G[x].append(tmp)
        G[x].appendleft(G[x].pop())
    if x + 1 < 5 and G[x + 1][6] != r and not visit[x + 1]: # 오른쪽
        dfs(x + 1, d * -1)
    if x - 1 > 0 and G[x - 1][2] != l and not visit[x - 1]: # 왼쪽
        dfs(x - 1, d * -1)
                
# 0: N극, 1: S극
G = [[0]]+ [deque(map(int, list(input()))) for _ in range(4)]
K = int(input())
visit = [False] * 5
adj = [[], [2], [1, 3], [2, 4], [3]]
score = 0
for _ in range(K):
    x, d = map(int, input().split())
    visit = [False] * 5
    dfs(x, d)
s = 1
for x in range(1, 5):
    if G[x][0]: score += s
    s *= 2
print(score)