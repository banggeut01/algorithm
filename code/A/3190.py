# 3190.py 뱀
def game():
    global second
    dir = 0  # 방향
    hx, hy = dq[0][0], dq[0][1]
    for _ in range(L):
        time, ch = input().split()
        time = int(time)
        s = time - second + 1
        for _ in range(s):
            hr, hc = hx + d[dir][0], hy + d[dir][1]
            if -1 < hr < N and -1 < hc < N:
                if not board[hr][hc]: # 사과가 아니면,
                    # 꼬리빼주기
                    tx, ty = dq.pop()
                    board[tx][ty] = 0
                # 머리 이동
                if board[hr][hc] == 2: # 뱀
                    return
                board[hr][hc] = 2
                dq.appendleft((hr, hc))
                hx, hy = hr, hc
            else:
                return
            second += 1
        # 직진 다하고, 방향을 틀어줘야함
        if ch == 'L': # 왼쪽
            dir = left[dir]
        else: # 오른쪽
            dir = right[dir]




from collections import deque
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
board = [[0] * N for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
left = [3, 0, 1, 2]
right = [1, 2, 3, 0]
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1 # 사과
dq = deque() # 0 머리, -1 꼬리
board[0][0] = 2 # 뱀
dq.append((0, 0))
L = int(input())
second = 1  # 총 시간
game()
print(second)