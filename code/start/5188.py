# 5188.py 최소합

def move_board(i, j, total): # ij:좌표, total:합
    global MIN, R, D

    if total > MIN:
        return

    if R == 0 and D == 0:
        MIN = min(MIN, total)
        return

    if R > 0: # 오른쪽으로 이동
        R -= 1
        move_board(i, j + 1, total + board[i][j + 1])
        R += 1
    if D > 0: # 아래로이동
        D -= 1
        move_board(i + 1, j, total + board[i + 1][j])
        D += 1

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    R = D = N - 1 # R:오른쪽 이동 가능 횟수, D:아래
    MIN = (R + D)  * 10 # MIN:답
    move_board(0, 0, board[0][0])
    print('#{} {}'.format(tc, MIN))