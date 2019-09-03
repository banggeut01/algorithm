# 4615.py 재미있는 오셀로 게임
import sys
sys.stdin = open('4615input.txt', 'r')

def othello(i, j, color): # ij: 탐색 위치, c: color
    global bcnt, wcnt

    for idx in range(8): # 8방향에 대해
        r, c = i + x[idx], j + y[idx]
        # 다른색 돌 찾으면, 돌 교체하며 전진
        tmp = []
        while 0 <= r < n and 0 <= c < n and board[r][c] != 0 and board[r][c] != color:
            tmp.append([board[r][c], r, c])
            board[r][c] = color
            bcnt, wcnt = bcnt + cnt[color - 1][0], wcnt + cnt[color - 1][1]
            r, c = r + x[idx], c + y[idx]
        # 교체한게 맞는경우
        if 0 <= r < n and 0 <= c < n and board[r][c] == color:
            continue # 냅두기
        # 아닌경우 되돌리기
        for origin, row, col in tmp:
            board[row][col] = origin
            bcnt, wcnt = bcnt + cnt[origin - 1][0], wcnt + cnt[origin - 1][1]

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n:보드길이, m:돌횟수
    # 보드 세팅
    board = [[0] * n for _ in range(n)]
    init, idx = [2, 1, 1, 2], 0
    for i in range(n // 2 - 1, n // 2 + 1):
        for j in range(n // 2 - 1, n // 2 + 1):
            board[i][j] = init[idx]
            idx += 1

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    bcnt = wcnt = 2
    cnt = [[1, -1], [-1, 1]] # cnt[0]: 흑돌 증가, cnt[1]: 백돌 증가
    for _ in range(m):
        i, j, stone = map(int, input().split()) # ij: 돌위치, stone:돌색
        i, j = i - 1, j - 1 # 인덱스 맞추기
        board[i][j] = stone
        if stone == 1:
            bcnt += 1
        else:
            wcnt += 1
        othello(i, j, stone)

    print('#{} {} {}'.format(tc, bcnt, wcnt))