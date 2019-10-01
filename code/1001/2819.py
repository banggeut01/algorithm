# 2819.py 격자판의 숫자 이어 붙이기

def dfs(i, j, tmp, k):
    if k == 6:
        case.add(tmp)
        return
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        r, c = i + dx, j + dy
        if -1 < r < 4 and -1 < c < 4:
            dfs(r, c, tmp + board[r][c], k + 1)

t = int(input())
for tc in range(1, t + 1):
    board = [list(input().split()) for _ in range(4)]
    case = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j], 0)
    print('#{} {}'.format(tc, len(case)))