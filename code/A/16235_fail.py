# 16235_fail.py 나무 재테크

import collections
N, M, K = map(int, input().split()) # N: 땅크기, M: 나무 개수, K: 연수
tree = collections.deque()
# die = collections.deque()
board = [[5] * (N + 1) for _ in range(N + 1)]
A = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)] # 양분
move = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j, a = map(int, input().split()) # 좌표, 나이
    tree.append((i, j, a))
tree = collections.deque(sorted(tree)) # 정렬
tree.append((0, 0, 0))
cnt = 0
while True:
    # 봄
    i, j, a = tree.popleft() #### 비었는지 검사
    while i + j + a != 0:
        if board[i][j] >= a: # 나이먹기
            board[i][j] -= a
            a += 1
            tree.append((i, j, a))
        else: # die
            # die.append((i, j, a // 2))
            move[i][j] = a // 2
        i, j, a = tree.popleft()
    # print('봄')
    # print(tree)
    tree.append((0, 0, 0))

    # 여름
    # while die:
    #     i, j, a = die.popleft()
    #     board[i][j] += a
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] += move[i][j]
            move[i][j] = 0
    # 가을
    i, j, a = tree.popleft()
    while i + j + a != 0:
        if a and not a % 5: # 번식
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                r, c = i + dx, j + dy
                if 0 < r < N + 1 and 0 < c < N + 1:
                    tree.append((r, c, 1))
        tree.append((i, j, a))
        i, j, a = tree.popleft()
    # print('가을')
    # print(tree)
    # 겨울
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] += A[i][j]

    cnt += 1
    if cnt == K: # K년
        break
    if not len(tree): # 산 나무 없으면,
        break
    tree = collections.deque(sorted(tree)) # 정렬
    tree.append((0, 0, 0))
print(len(tree))

