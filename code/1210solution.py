# ladder 풀이 1210solution.py

import sys
sys.stdin = open('1210input.txt', 'r')


def DFS(x, y):
    if x == 0: return y

    arr[x][y] = 0
    if y - 1 >= 0 and arr[x][y - 1]:
        return arr(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return arr(x, y + 1)
    else:
        return arr(x + 1, y)

for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0 # x열, y:열

    for i in range(100):
        if arr[99][j] == 2:
            x, y = 99, i
            break

    # dir = 0 # direction 0: 위, 1: 왼쪽, 2: 오른쪽
    # while x:
    #     if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
    #         y, dir = y - 1, 1
    #     elif dir != 1 and y + 1 < 100 and arr[x][y + 1]:
    #         y, dir = y + 1, 2
    #     else:
    #         x, dir = x - 1, 0

    # while x:
    #     if y - 1 >= 0 and arr[x][y - 1]:
    #         while y - 1 >= 0 and arr[x][y - 1]:
    #             y -= 1
    #     elif y + 1 < 100 and arr[x][y + 1]:
    #         while y + 1 < 0 and arr[x][y - 1]:
    #             y += 1
    #     x -= 1

        print(y)