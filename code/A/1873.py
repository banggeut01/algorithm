# 1873.py 상호의 배틀필드
import sys
sys.stdin = open('1873input.txt', 'r')

def battle_game(i, j): #i,j 전차위치
    global h, w

    for act in actions:
        if act == 'U':
            mymap[i][j] = '^' #방향바꾸기
            if 0 <= i - 1 and mymap[i - 1][j] == '.': # 평지면,
                mymap[i][j], mymap[i - 1][j] = mymap[i - 1][j], mymap[i][j] # 이동
                i -= 1
        elif act == 'D':
            mymap[i][j] = 'v'
            if i + 1 < h and mymap[i + 1][j] == '.':
                mymap[i][j], mymap[i + 1][j] = mymap[i + 1][j], mymap[i][j]
                i += 1
        elif act == 'L':
            mymap[i][j] = '<'
            if 0 <= j - 1 and mymap[i][j - 1] == '.':
                mymap[i][j], mymap[i][j - 1] = mymap[i][j - 1], mymap[i][j]
                j -= 1
        elif act == 'R':
            mymap[i][j] = '>'
            if j + 1 < w and mymap[i][j + 1] == '.':
                mymap[i][j], mymap[i][j + 1] = mymap[i][j + 1], mymap[i][j]
                j += 1
        else: # act == 'S':
            if mymap[i][j] == '^':
                r, c = i - 1, j
                while 0 <= r:
                    if mymap[r][c] == '#': # 강철
                        break
                    elif mymap[r][c] == '*': # 벽돌
                        mymap[r][c] = '.' # 평지로 바뀜
                        break
                    r -= 1
            elif mymap[i][j] == 'v':
                r, c = i + 1, j
                while r < h:
                    if mymap[r][c] == '#': # 강철
                        break
                    elif mymap[r][c] == '*': # 벽돌
                        mymap[r][c] = '.' # 평지로 바뀜
                        break
                    r += 1
            elif mymap[i][j] == '<':
                r, c = i, j - 1
                while 0 <= c:
                    if mymap[r][c] == '#': # 강철
                        break
                    elif mymap[r][c] == '*': # 벽돌
                        mymap[r][c] = '.' # 평지로 바뀜
                        break
                    c -= 1
            else: # '>'
                r, c = i, j + 1
                while c < w:
                    if mymap[r][c] == '#': # 강철
                        break
                    elif mymap[r][c] == '*': # 벽돌
                        mymap[r][c] = '.' # 평지로 바뀜
                        break
                    c += 1

t = int(input())
for tc in range(1, t + 1):
    h, w = map(int, input().split()) # 맵 높이,너비
    mymap = [list(input()) for _ in range(h)]
    tank = ['^', 'v', '<', '>'] # 전차 상태
    n = int(input()) # 동작 개수
    actions = input() # 동작

    # 전차 찾기
    flag = 0
    for i in range(h):
        for j in range(w):
            if mymap[i][j] in tank: # 전차 찾음
                flag = 1
                battle_game(i, j)
                break
        if flag:
            break
    print('#{} '.format(tc), end='')
    for i in range(h):
        print(''.join(mymap[i]))
