# 4875.py 미로
# DFS로 풀어보자.

import sys
sys.stdin = open('4875input.txt', 'r')

def maze(i, j):
    global n, result

    my_map[i][j] = 1

    for idx in range(4):
        row, col = i + x[idx], j + y[idx]
        if -1 < row < n and -1 < col < n:
            if my_map[row][col] == 3:
                result = 1
            elif my_map[row][col] == 0:
                maze(row, col)

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    my_map = [[] for _ in range(n)]
    for idx in range(n):
        inputline = input()
        for c in inputline:
            my_map[idx].append(int(c))

    # 상하좌우
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]

    result = 0 # 답

    flag = 0
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 2:
                maze(i, j)
                flag = 1
                break
        if flag == 1:
            break

    print('#{} {}'.format(tc, result))
