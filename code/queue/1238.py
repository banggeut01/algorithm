# 1238.py Contact
# 유향
# BFS

import collections
import sys
sys.stdin = open('1238input.txt', 'r')

def bfs(s):
    global max_d

    visit[s] = True
    dq = collections.deque()
    dq.append(s)

    while dq:
        node = dq.popleft()
        for w in adj[node]:
            if not visit[w]:
                visit[w] = True
                dq.append(w)
                d[w] = d[node] + 1
                max_d = max(d[w], max_d)
                print(d)

for tc in range(1, 11):
    n, s = map(int, input().split()) # 입력 데이터 길이, 노드 시작점
    data = list(map(int, input().split()))
    adj = [[] for _ in range(101)] # 번호 1~100
    visit = [False] * (101)
    d = [0] * 101 # 거리
    max_d = 0

    for i in range(n // 2):
        adj[data[i * 2]].append(data[i * 2 + 1])

    bfs(s)

    max_num = 0
    for i in range(1, 101):
        if max_d == d[i]:
            max_num = max(max_num, i)
    print('#{} {}'.format(tc, max_num))

