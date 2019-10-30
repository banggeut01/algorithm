# 큐빙 5373.py

import copy

# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# '-': 반시계 방향, '+': 시계 방향
def rotationLeft(x, y):
    # 반시계방향
    tmp = [[0] * 9 for _ in range(12)]
    for i in range(3):
        for j in range(3):
            tmp[x + i][y + j] = cube[x + j][y + 2 - i]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            cube[i][j] = tmp[i][j]

# 원래           시계          반시계
# 30, 31, 32    50, 40, 30    32, 42, 52
# 40, 41, 42    51, 41, 31    31, 41, 51
# 50, 51, 52    52, 42, 32    30, 40, 50
#
# 33, 34, 35    35, 45, 55
# 43, 44, 45    34, 44, 54
# 53, 54, 55    33, 43, 53

def rotationRight(x, y):
    # 시계방향
    tmp = [[0] * 9 for _ in range(12)]
    for i in range(3):
        for j in range(3):
            tmp[x + i][y + j] = cube[x + 2 - j][y + i]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            cube[i][j] = tmp[i][j]

def rotationCube(plane, dir): # 돌린 면, 회전 방향

    if plane == 'L':
        if dir == '-': # 반시계
            t1, t2, t3 = cube[9][3], cube[10][3], cube[11][3]
            for x in range(9):
                cube[x - 3][3] = cube[x][3]
            cube[6][3], cube[7][3], cube[8][3] = t1, t2, t3
            rotationLeft(3, 0)
        else: # 시계
            t1, t2, t3 = cube[9][3], cube[10][3], cube[11][3]
            for x in range(11, 2, -1):
                cube[x][3] = cube[x - 3][3]
            cube[0][3], cube[1][3], cube[2][3] = t1, t2, t3
            rotationRight(3, 0)

    elif plane == 'R': # 오른쪽
        if dir == '+': # 시계
            t1, t2, t3 = cube[9][5], cube[10][5], cube[11][5]
            for x in range(9):
                cube[x - 3][5] = cube[x][5]
            cube[6][5], cube[7][5], cube[8][5] = t1, t2, t3
            rotationLeft(3, 6)
        else:  # 시계
            t1, t2, t3 = cube[9][5], cube[10][5], cube[11][5]
            for x in range(11, 2, -1):
                cube[x][5] = cube[x - 3][5]
            cube[0][5], cube[1][5], cube[2][5] = t1, t2, t3
            rotationRight(3, 6)

    elif plane == 'B':
        if dir == '+':
            t1, t2, t3 = cube[3][0], cube[3][1], cube[3][2]
            for x in range(6):
                cube[3][x] = cube[3][x + 3]
            cube[3][6], cube[3][7], cube[3][8] = cube[11][3], cube[11][4], cube[11][5]
            cube[11][3], cube[11][4], cube[11][5] = t1, t2, t3
            rotationRight(0, 3)

        else:
            t1, t2, t3 = cube[3][8], cube[3][7], cube[3][6]
            for x in range(8, 2, -1):
                cube[3][x] = cube[3][x - 3]
            cube[3][2], cube[3][1], cube[3][0] = cube[11][3], cube[11][4], cube[11][5]
            cube[11][3], cube[11][4], cube[11][5] = t1, t2, t3

            rotationLeft(0, 3)

    elif plane == 'F':
        if dir == '-':
            t1, t2, t3 = cube[5][0], cube[5][1], cube[5][2]
            for x in range(6):
                cube[5][x] = cube[5][x + 3]
            cube[5][6], cube[5][7], cube[5][8] = cube[9][3], cube[9][4], cube[9][5]
            cube[9][3], cube[9][4], cube[9][5] = t1, t2, t3
            rotationLeft(6, 3)
        else:
            t1, t2, t3 = cube[5][8], cube[5][7], cube[5][6]
            for x in range(8, 2, -1):
                cube[5][x] = cube[5][x - 3]
            cube[5][2], cube[5][1], cube[5][0] = cube[9][3], cube[9][4], cube[9][5]
            cube[9][3], cube[9][4], cube[9][5] = t1, t2, t3
            rotationRight(6, 3)

    elif plane == 'U':
        if dir == '+':
            t1, t2, t3 = cube[3][6], cube[4][6], cube[5][6]
            cube[3][6], cube[4][6], cube[5][6] = cube[2][3], cube[2][4], cube[2][5]
            cube[2][3], cube[2][4], cube[2][5] = cube[5][2], cube[4][2], cube[3][2]
            cube[5][2], cube[4][2], cube[3][2] = cube[6][5], cube[6][4], cube[6][3]
            cube[6][5], cube[6][4], cube[6][3] = t1, t2, t3
            rotationRight(3, 3)
        else:
            t1, t2, t3 = cube[6][5], cube[6][4], cube[6][3]
            cube[6][5], cube[6][4], cube[6][3] = cube[5][2], cube[4][2], cube[3][2]
            cube[5][2], cube[4][2], cube[3][2] = cube[2][3], cube[2][4], cube[2][5]
            cube[2][3], cube[2][4], cube[2][5] = cube[3][6], cube[4][6], cube[5][6]
            cube[3][6], cube[4][6], cube[5][6] = t1, t2, t3
            rotationLeft(3, 3)

    else: # plane 'D'
        if dir == '-':
            t1, t2, t3 = cube[0][3], cube[0][4], cube[0][5]
            cube[0][3], cube[0][4], cube[0][5] = cube[5][0], cube[4][0], cube[3][0]
            cube[5][0], cube[4][0], cube[3][0] = cube[8][5], cube[8][4], cube[8][3]
            cube[8][5], cube[8][4], cube[8][3] = cube[3][8], cube[4][8], cube[5][8]
            cube[3][8], cube[4][8], cube[5][8] = t1, t2, t3
            rotationLeft(9, 3)
        else:
            t1, t2, t3 = cube[0][3], cube[0][4], cube[0][5]
            cube[0][3], cube[0][4], cube[0][5] = cube[3][8], cube[4][8], cube[5][8]
            cube[3][8], cube[4][8], cube[5][8] = cube[8][5], cube[8][4], cube[8][3]
            cube[8][5], cube[8][4], cube[8][3] = cube[5][0], cube[4][0], cube[3][0]
            cube[5][0], cube[4][0], cube[3][0] = t1, t2, t3
            rotationRight(9, 3)

initCube = [[0, 0, 0, 'o', 'o', 'o', 0, 0, 0],              # [0][0~9]
            [0, 0, 0, 'o', 'o', 'o', 0, 0, 0],
            [0, 0, 0, 'o', 'o', 'o', 0, 0, 0],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],  # [3]
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            [0, 0, 0, 'r', 'r', 'r', 0, 0, 0],              # [6]
            [0, 0, 0, 'r', 'r', 'r', 0, 0, 0],
            [0, 0, 0, 'r', 'r', 'r', 0, 0, 0],
            [0, 0, 0, 'y', 'y', 'y', 0, 0, 0],              # [9]
            [0, 0, 0, 'y', 'y', 'y', 0, 0, 0],
            [0, 0, 0, 'y', 'y', 'y', 0, 0, 0]]

import pprint

t = int(input())
for _ in range(t):
    tc = int(input())
    act = list(input().split())
    cube = copy.deepcopy(initCube)
    for idx in range(len(act)):
        rotationCube(act[idx][0], act[idx][1])
        print('# {}'.format(idx+1))
        pprint.pprint(cube)
        print()
    for i in range(3, 6):
        print(''.join(map(str, cube[i][3:6])))

