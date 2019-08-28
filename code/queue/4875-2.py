# 미로 4875-2.py
# BFS

import sys, collections
sys.stdin = open('4875input.txt', 'r')

def bfs(i, j):
    dq = collections.deque()
    my_map[i][j] = 1 # 방문
    dq.append((i, j))
    
    while dq: # 빈큐 아닐동안,
        i, j = dq.popleft()
        for idx in range(4): # 인접 정점
            a, b = i + x[idx], j + y[idx]
            if -1 < a < n and -1 < b < n:
                if my_map[a][b] == 3:
                    return 1
                elif not my_map[a][b]: # 방문안한 정점
                    my_map[a][b] = 1 # 방문
                    dq.append((a, b))

    return 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    # 상하좌우
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]

    my_map = [[] for _ in range(n)]
    for i in range(n):
        inputline = input()
        for ele in inputline:
            my_map[i].append(int(ele))


    # 시작점 찾기
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 2:
                result = bfs(i, j)
                break

    print('#{} {}'.format(tc, result))