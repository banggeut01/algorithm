# 16235.py 나무 재테크

import collections
N, M, K = map(int, input().split()) # N: 땅크기, M: 나무 개수, K: 연수
tree = collections.deque()
die = collections.deque()
A = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)] # 양분
print(A)
for _ in range(M):
    i, j, a = map(int, input().split()) # 좌표, 나이
    tree.append((i, j, a))
tree = sorted(tree) # 정렬
tree.append((0, 0, 0))
# 봄
i, j, a = tree.popleft() #### 비었는지 검사
while i + j + a != 0:
    if A[i][j] >= a: # 나이먹기
        a += 1
        A[i][j] -= a
        tree.append((i, j, a))
    else: # die
        die.append((i, j, a // 2))
    i, j, a = tree.popleft()
tree.append((0, 0, 0))

# 여름
while die:
    i, j, a = die.popleft()
    A[i][j] += a
# 가을
i, j, a = tree.popleft()
while i + j + a != 0:
    if not a % 5: # 번식
        for dx, dy in
    i, j, a = tree.popleft()
tree.append((0, 0, 0))