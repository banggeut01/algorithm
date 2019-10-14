# 16235.py 나무 재테크

import collections
N, M, K = map(int, input().split()) # N: 땅크기, M: 나무 개수, K: 연수
tree = [[collections.deque() for _ in range(N + 1)] for _ in range(N + 1)] # 나이 오름차순
board = [[5] * (N + 1) for _ in range(N + 1)]
A = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)] # 양분
move = [[0] * (N + 1) for _ in range(N + 1)] # 죽은 나무 => 양분
tcnt = 0
for _ in range(M):
    i, j, a = map(int, input().split()) # 좌표, 나이
    tree[i][j].append(a)
    tcnt += 1
year = 0

while True:
    # 봄
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not tree[i][j]: continue
            x = 0
            while x < len(tree[i][j]) and board[i][j] >= tree[i][j][x]:
                board[i][j] -= tree[i][j][x]
                tree[i][j][x] += 1
                x += 1
            while x != len(tree[i][j]):
                move[i][j] += tree[i][j][x] // 2
                tree[i][j].pop()
                tcnt -= 1
    # # 여름
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if move[i][j]:
                board[i][j] += move[i][j]
                move[i][j] = 0
    # # 가을
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not tree[i][j]: continue
            for x in range(len(tree[i][j])):
                if tree[i][j][x] % 5: continue
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    r, c = i + dx, j + dy
                    if 0 < r < N + 1 and 0 < c < N + 1:
                        tree[r][c].appendleft(1)
                        tcnt += 1
    # 겨울
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] += A[i][j]

    year += 1
    if year == K: # K년
        break
    if not tcnt: break
print(tcnt)
'''
10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1
답: 5443
'''