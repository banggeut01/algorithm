import sys
from typing import List

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split()) # n:행, m:열, k:칠 횟수
    my_map = [[0] * m for _ in range(n)]

    for _ in range(k):
        x1, y1, x2, y2, color = map(int, input().split())
        flag = 0
        for row in range(y1, y2 + 1):
            for col in range(x1, x2 + 1):
                if my_map[row][col] > color:
                    flag = 1
                    break
            if flag == 1:
                break
        if not flag:
            for row in range(y1, y2 + 1):
                for col in range(x1, x2 + 1):
                    my_map[row][col] = color

    p = [0] * 11
    for row in range(n):
        for col in range(m):
            p[my_map[row][col]] += 1

    max_cnt = max(p)


    print('#{} {}'.format(tc, max_cnt))

