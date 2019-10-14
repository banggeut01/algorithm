# 16235.py 나무 재테크

import collections
N, M, K = map(int, input().split()) # N: 땅크기, M: 나무 개수, K: 연수
tree = [[collections.deque() for _ in range(N + 1)] for _ in range(N + 1)] # 나이 오름차순
board = [[5] * (N + 1) for _ in range(N + 1)]
A = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)] # 양분
tcnt = 0
for _ in range(M):
    i, j, a = map(int, input().split()) # 좌표, 나이
    tree[i][j].append(a)
    tcnt += 1

for _ in range(K):
    # 봄, 여름
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for x in range(len(tree[i][j])):
                if board[i][j] >= tree[i][j][x]:
                    board[i][j] -= tree[i][j][x]
                    tree[i][j][x] += 1
                else:
                    while x < len(tree[i][j]):
                        board[i][j] += tree[i][j].pop() // 2
                        tcnt -= 1
                    break
    # 가을, 겨울
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for x in range(len(tree[i][j])):
                if not tree[i][j][x] % 5:
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                        r, c = i + dx, j + dy
                        if 0 < r < N + 1 and 0 < c < N + 1:
                            tree[r][c].appendleft(1)
                            tcnt += 1
            board[i][j] += A[i][j]

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