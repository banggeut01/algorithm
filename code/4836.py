# 색칠하기 4836.py
import sys
sys.stdin = open('4836input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    # 좌표, 0-무색, 1-빨강, 2-파랑, 3-보라
    grid = [[0]*10 for _ in range(10)]
    # 보라 영역 카운트
    cnt = 0

    for _ in range(n):
        # 입력값: 왼쪽 위/오른쪽 아래 인덱스, 칠할 색상
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1): # 위 -> 아래로 r1~r2
            for j in range(c1, c2+1): # 왼쪽 -> 오른쪽 c1~c2
                # 보라 제외하고, grid, color 다른색인 경우
                if grid[i][j] != color and grid[i][j] != 3:
                    # 색 더해주기
                    grid[i][j] += color
                    # 보라색으로 바뀐 경우
                    if grid[i][j] == 3:
                        cnt += 1


    print('#{} {}'.format(tc, cnt))