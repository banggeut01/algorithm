# 2615.py 오목
import sys
sys.stdin = open('2615input.txt', 'r')

def row_check(i, j, stn): # ij: 시작위치, stn(stone): 바둑알
    if (j - 1 > -1 and board[i][j] != board[i][j - 1]) or j == 0:
        for x in range(1, 5):
            if 0 < j + 1 < 19 and board[i][j + x] == stn:
                continue
            else:
                return False
        if (j + 5 < 19 and board[i][j + 5] != stn) or j + 5 == 19:
            return stn
        else:
            return False
    else:
        return False

def col_check(i, j, stn):
    if (i - 1 > -1 and board[i][j] != board[i - 1][j]) or i == 0:
        for x in range(1, 5):
            if 0 < i + x < 19 and board[i + x][j] == stn:
                continue
            else:
                return False
        if (i + 5 < 19 and board[i + 5][j] != stn) or i + 5 == 19:
            return stn
        else:
            return False
    else:
        return False


def cross_check(i, j, stn):
    if (i - 1 > -1 and j - 1 > - 1 and board[i][j] != board[i - 1][j - 1]) or i == 0 or j == 0:
        for x in range(1, 5):
            if -1 < i + x < 19 and -1 < j + x < 19 and board[i + x][j + x] == stn:
                continue
            else:
                return False
        if (i + 5 < 19 and j + 5 < 19 and board[i + 5][j + 5] != stn) or i + 5 == 19 or j + 5 == 19:
            return stn
        else:
            return False
    else:
        return False


def rvs_cross_check(i, j, stn):
    if (i - 1 > -1 and j + 1 < 19 and board[i][j] != board[i - 1][j + 1]) or i == 0 or j == 18:
        for x in range(1, 5):
            if -1 < i + x < 19 and -1 < j - x < 19 and board[i + x][j - x] == stn:
                continue
            else:
                return False
        if (i + 5 < 19 and j - 5 > -1 and board[i + 5][j - 5] != stn) or i + 5 == 19 or j - 5 == -1:
            return stn
        else:
            return False
    else:
        return False


board = [list(map(int, input().split())) for _ in range(19)]

flag = 0
result = False
for i in range(19):
    for j in range(15):
        if board[i][j] != 0:
            result = row_check(i, j, board[i][j])  # ij: 시작위치, stone- 검1, 흰2
            if result:
                flag = 1
                break
            else:
                result = col_check(j, i, board[j][i])
                if result:
                    i, j = j, i
                    flag = 1
                    break
    if flag:
        break

if not flag:
    for i in range(15):
        for j in range(15):
            if board[i][j] != 0:
                result = cross_check(i, j, board[i][j])
                if result:
                    flag = 1
                    break
        if flag:
            break

if not flag:
    for i in range(15):
        for j in range(4, 19):
            if board[i][j] != 0:
                result = rvs_cross_check(i, j, board[i][j])
                if result:
                    i, j = i + 4, j - 4
                    flag = 1
                    break
        if flag:
            break

if flag == 1:
    print(result)
    print(i + 1, j + 1)
else:
    print(0)

