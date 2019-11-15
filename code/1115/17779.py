# 17779.py 게리맨더링 2

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 총 인구수
total = 0
for x in range(N):
    for y in range(N):
        total += board[x][y]

MIN = total # 답
for x in range(N):
    for y in range(N):
        for d1 in range(1, N): # d1: 1~N-1
            for d2 in range(1, N): # d2: 1~N-1
                if 0 <= x < x + d1 + d2 < N and 0 <= y - d1 < y < y + d2 < N:
                    p = [0] * 6  # 1 ~5 선거구 인구수
                    # 1 선거구
                    for i in range(x): # 0~x-1
                        for j in range(y + 1): # 0~y
                            p[1] += board[i][j]
                    s = 1
                    for i in range(x, x + d1): # x ~ x+d1-1
                        for j in range(y - s + 1): # 0~y-s
                            if j < 0: break
                            p[1] += board[i][j]
                        s += 1
                    # 2 선거구
                    for i in range(x + 1): # 0~x
                        for j in range(y + 1, N): # y+1~N-1
                            p[2] += board[i][j]
                    s = 1
                    for i in range(x + 1, x + d2 + 1): # x+1 ~ x+d2
                        for j in range(y + 1 + s, N): # y+s ~ N-1
                            p[2] += board[i][j]
                        s += 1
                    # 3 선거구
                    s = 1
                    for i in range(x + d1 + d2, x + d1 - 1, -1): # x+d1+d2 ~ x+d1
                        for j in range(y - d1 + d2 - s + 1): # 0 ~ y-s
                            if j < 0: break
                            p[3] += board[i][j]
                        s += 1
                    for i in range(x + d1 + d2 + 1, N): # x+d1+d2+1 ~ N-1
                        for j in range(y - d1 + d2): # 0 ~ y-d1+d2
                            p[3] += board[i][j]
                    # 4 선거구
                    s = 1
                    for i in range(x + d1 + d2, x + d2, -1): # x+d1+d2 ~ x+d2+1
                        # s = 1
                        for j in range(y - d1 + d2 + s, N): # y+s ~ N - 1
                            p[4] += board[i][j]
                        s += 1
                    for i in range(x + d1 + d2 + 1, N): # x+d1+d2+1 ~ N-1
                        for j in range(y - d1 + d2, N): # y ~ N - 1
                            p[4] += board[i][j]
                    p[5] = total - (p[1] + p[2] + p[3] + p[4])
                    MIN = min(MIN, max(p[1:]) - min(p[1:]))
print(MIN)