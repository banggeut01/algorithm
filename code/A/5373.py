# 큐빙 5373.py
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# '-': 반시계 방향, '+': 시계 방향
def rotationLeft(x, y):
    tmp = [[0] * 9 for _ in range(12)]
    # 반시계방향
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            tmp[x][y] = cube[y][3 - 1 - x]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            cube[x][y] = tmp[x][y]

def rotationRight(x, y):
    tmp = [[0] * 9 for _ in range(12)]
    # 반시계방향
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            tmp[x][y] = cube[3 - 1 - y][x]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            cube[x][y] = tmp[x][y]

def rotationCube(plane, dir): # 돌린 면, 회전 방향
    if plane == 'L':
        if dir == '-': # [3]
            tmp = cube[0][:3]
            for x in range(9):
                cube[x][3] = cube[x + 1][3]
            for x in range(3)
            cube[11][3] = tmp
            rotationLeft(3, 3)
        else:
            tmp = cube[11][3]
            for x in range(11):
                cube[x + 1][3] = cube[x][3]
            cube[0][3] = tmp
            rotationRight(3, 3)

cube = [[0, 0, 0, 'o', 'o', 'o', 0, 0, 0],              # [0][0~9]
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


t = int(input())
for _ in range(t):
    tc = int(input())
    act = list(input().split())
    print(act)
    for idx in range(len(act)):
        rotationCube(act[idx][0], act[idx][1])
    for i in range(3, 6):
        print(''.join(map(str, cube[i][3:6])))
    import pprint
    pprint.pprint(cube)