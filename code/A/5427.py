# 5472.py 불
import collections
import sys
sys.stdin = open('5427input.txt', 'r')

def bfs():
    global w, h

    while dq:
        n = dq.popleft() # node, [0]~[2]
        if not n[0]: # 불이면,
            for i in range(4): # 4방향에 대해서
                r, c = n[1] + x[i], n[2] + y[i]
                if 0 <= r < h and 0 <= c < w and mymap[r][c] == '.':
                    visit[r][c] = True
                    mymap[r][c] = '*'
                    dq.append((0, r, c))
        else: # 상근
            for i in range(4):
                r, c = n[1] + x[i], n[2] + y[i]
                if r == -1 or c == -1 or r == h or c == w:
                    return D[n[1]][n[2]] + 1
                if 0 <= r < h and 0 <= c < w and not visit[r][c]:
                    visit[r][c] = True
                    dq.append((1, r, c))
                    D[r][c] = D[n[1]][n[2]] + 1

    return 'IMPOSSIBLE'

t = int(input())
for tc in range(1, t + 1):
    w, h = map(int, input().split()) # w:너비, h:높이
    visit = [[False] * w for _ in range(h)] # 상근이가 갈 수 있는지
    mymap = [list(input()) for _ in range(h)]
    D = [[0] * w for _ in range(h)]
    dq = collections.deque() # [0]: type(0:불,1:나), [1]: row, [2]: col
    x = [0, 0, -1, 1] # 상하좌우
    y = [-1, 1, 0, 0]
    # visit 초기화
    for i in range(h):
        for j in range(w):
            if mymap[i][j] != '.':
                visit[i][j] = True
            if mymap[i][j] == '*':
                dq.appendleft((0, i, j)) # 불 먼저
            elif mymap[i][j] == '@':
                mymap[i][j] = '.'
                dq.append((1, i, j))

    print(bfs())

