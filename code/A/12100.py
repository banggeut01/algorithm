# 12100.py 2048(Easy)
from collections import deque

def dfs(b, k):
    if k == 5:
        global MAX
        maxB = 0
        for i in range(N):
            for j in range(N):
                maxB = max(maxB, b[i][j])
        MAX = max(MAX, maxB)
        return
    tmp = deque()
    # 위
    nb = [[0] * N for _ in range(N)]
    s, e, d = 0, N - 1, 1
    for j in range(N):
        prev = 0
        for i in range(s, e + d, d):
            cur = b[i][j]
            if not prev:
                if cur:
                    prev = cur
            else:
                if prev == cur:
                    tmp.append(cur * 2)
                    prev = 0
                else:
                    if cur:
                        tmp.append(prev)
                        prev = cur
        if prev: tmp.append(prev)
        i = s
        while tmp:
            nb[i][j] = tmp.popleft()
            i += d
    dfs(nb, k + 1)
    # 아래
    nb = [[0] * N for _ in range(N)]
    s, e, d = N - 1, 0, -1
    for j in range(N):
        prev = 0
        for i in range(s, e + d, d):
            cur = b[i][j]
            if not prev:
                if cur:
                    prev = cur
            else:
                if prev == cur:
                    tmp.append(cur * 2)
                    prev = 0
                else:
                    if cur:
                        tmp.append(prev)
                        prev = cur
        if prev: tmp.append(prev)
        i = s
        while tmp:
            nb[i][j] = tmp.popleft()
            i += d
    dfs(nb, k + 1)
    # 왼쪽
    nb = [[0] * N for _ in range(N)]
    s, e, d = 0, N - 1, 1
    for i in range(N):
        prev = 0
        for j in range(s, e + d, d):
            cur = b[i][j]
            if not prev:
                if cur:
                    prev = cur
            else:
                if prev == cur:
                    tmp.append(cur * 2)
                    prev = 0
                else:
                    if cur:
                        tmp.append(prev)
                        prev = cur
        if prev: tmp.append(prev)
        j = s
        while tmp:
            nb[i][j] = tmp.popleft()
            j += d
    dfs(nb, k + 1)
    # 오른쪽
    nb = [[0] * N for _ in range(N)]
    s, e, d = N - 1, 0, -1
    for i in range(N):
        prev = 0
        for j in range(s, e + d, d):
            cur = b[i][j]
            if not prev:
                if cur:
                    prev = cur
            else:
                if prev == cur:
                    tmp.append(cur * 2)
                    prev = 0
                else:
                    if cur:
                        tmp.append(prev)
                        prev = cur
        if prev: tmp.append(prev)
        j = s
        while tmp:
            nb[i][j] = tmp.popleft()
            j += d
    dfs(nb, k + 1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
dfs(board, 0)
print(MAX)
