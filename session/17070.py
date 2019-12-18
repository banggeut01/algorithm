# 17070.py 파이프 옮기기 1
def isPossible(nx, ny):
    if -1 < nx < N and -1 < ny < N and not board[nx][ny]:
        return True
    return False

def bf(s, x, y): # s:status, 상태 가로0, 세로1, 대각선2
    if x == N - 1 and y == N - 1:
        global ANS
        ANS += 1
        return

    flag = True
    if isPossible(x, y + 1):
        if s != 1: bf(0, x, y + 1)
    else: flag = False
    if isPossible(x + 1, y):
        if s != 0: bf(1, x + 1, y)
    else: flag = False
    if isPossible(x + 1, y + 1) and flag: bf(2, x + 1, y + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# D = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]] # 가로0, 세로1, 대각선2
ANS = 0
bf(0, 0, 1)
print(ANS)
# 가로 -> 가로, 대각선
# 세로 -> 세로, 대각선
# 대각선 -> 가로, 세로, 대각선
