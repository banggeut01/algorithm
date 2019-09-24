# 백준 - 색종이 10163.py
n = int(input())

# 좌표 초기화
grid = [[0] * 101 for _ in range(101)]

for i in range(1, n + 1): # 1~n
    # 좌표, 너비, 높이
    r, c, width, height = map(int, input().split())
    for w in range(width):
        for h in range(height):
            grid[r+w][c+h] = i

for i in range(1, n + 1):
    cnt = 0
    for r in range(101):
        for c in range(101):
            if grid[r][c] == i:
                cnt += 1
    print(cnt)
    
