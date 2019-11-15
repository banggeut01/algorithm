# 17406. 배열 돌리기 4
import pprint
import copy

def rotation(i, j, l, board):
    x, y = i - l, j - l # 시작점
    tmp = board[x][y]
    while x < i + l:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
        x += 1
    while y < j + l:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
        y += 1
    while x > i - l:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
        x -= 1
    while y > j - l + 1:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
        y -= 1
    board[x][y] = tmp

def perm(k): # 연산 순서를 정함
    if k == K:
        global MIN
        board = copy.deepcopy(inputBoard)
        for i in range(K): # K번의 회전 연산
            r, c, s = li[seq[i]]
            for l in range(1, s + 1):
                rotation(r - 1, c - 1, l, board)
        for i in range(N):
            total = 0
            for j in range(M):
                total += board[i][j]
            MIN = min(MIN, total)
        # pprint.pprint(board)
        return

    for x in range(K):
        if not used[x]:
            used[x] = True
            seq.append(x)
            perm(k + 1)
            used[x] = False
            seq.pop()

N, M, K = map(int, input().split()) # 행,열,회전 연산 개수
inputBoard = [list(map(int, input().split())) for _ in range(N)]
li = [list(map(int, input().split())) for _ in range(K)] # K개 연산
# print(li)
seq = []
used = [False] * K
MIN = N * M * 100
perm(0)
# print(li)
print(MIN)