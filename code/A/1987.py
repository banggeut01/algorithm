# 1987.py 알파벳

def back(i, j, d):
    global ANS
    if ANS == 26: # 최대 알파벳 개수 26
        return
    ANS = max(d, ANS)
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        r, c = i + dx, j + dy
        if -1 < r < R and -1 < c < C \
                and not past[ord(board[r][c]) - 65] and not visit[r][c]:
            visit[r][c] = True
            past[ord(board[r][c]) - 65] = True
            back(r, c, d + 1)
            visit[r][c] = False
            past[ord(board[r][c]) - 65] = False

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visit = [[False] * C for _ in range(R)]
ANS = 0
past = [False] * 26
visit[0][0] = True
past[ord(board[0][0]) - 65] = True
back(0, 0, 1)
print(ANS)