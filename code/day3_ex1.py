# day3_ex1.py
arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

n, m = len(arr), len(arr[0]) # n:행, m:열

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

