# 1979.py 어디에 단어가 들어갈 수 있을까

def is_possible(i):
    global j

    idx = 0
    while j + idx < N and board[i][j + idx]:
        idx += 1
    j = j + idx
    if idx == K:
        return True
    else:
        return False

# t = 1
t = int(input())
for tc in range(1, t + 1):
    # N, K = 5, 3
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # board = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
    result = 0 # 답
    # print(board)
    # 가로검사
    for i in range(N):
        j = 0
        while j < N - K + 1:
            if board[i][j] and is_possible(i):
                # print(i, j)
                result += 1
            j = j + 1

    # 전치행렬
    for i in range(N):
        for j in range(i, N):
            board[i][j], board[j][i] = board[j][i], board[i][j]
    # print(board)
    # 세로검사
    for i in range(N):
        j = 0
        while j < N - K + 1:
            if board[i][j] and is_possible(i):
                # print(i, j)
                result += 1
            j = j + 1
    print('#{} {}'.format(tc, result))