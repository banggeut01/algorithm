# test3.py 섬의 개수 구하기 - 못품!

import sys
sys.stdin = open('ex3input.txt', 'r')

def dfs(i, j):
    my_map[i][j] = 0

    goto = [] # 8 방향 중 갈 수 있는 지면
    
    for m in range(8):
        # my_map[i+x[m]][j+y[m]]
        
        # 아래 세줄 필요 없음!
        tmp = []
        tmp.append(i + x[m])
        tmp.append(j + y[m])
        if n > tmp[0] > -1 and -1 <tmp[1] < n and my_map[tmp[0]][tmp[1]]:
            goto.append(tmp)

    for g in goto:
        dfs(g[0], g[1])




t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    my_map = [list(map(int, input().split())) for _ in range(n)]

    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [1, 1, 1, 0, 0, -1, -1, -1]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if my_map[i][j]: # 섬 시작!
                dfs(i, j)
                cnt += 1


    print(cnt)
   



