# 1242.py 암호코드 스캔

import sys
sys.stdin = open('1242input.txt', 'r')

def find_endidx(i, j):
    while True:
        j += 1
        if j + 1 >= M:
            break
        elif j + 1 < M and board[i][j + 1] == 0 and j + 2 
    while i < N and board[i][j - 1] != '0':
        i += 1
    return (i, j)

def update_board(i, j, endi, endj):
    for r in range(i, endi):
        for c in range(j, endj):
            board[r][c] = '0'

# 암호 번호
num = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
        [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # 행,열 크기
    board = [list(input()) for _ in range(N)]
    code = []  # 암호코드
    for i in range(N):
        for j in range(M):
            if board[i][j] != '0':
                endi, endj = find_endidx(i, j)
                hex_code = ''.join(board[i][j:endj]) # 16진수 코드
                update_board(i, j, endi, endj)
                dec_code = int('0x' + hex_code, 16) # 10진수 코드
                bin_code = bin(dec_code) # 2진수 코드
                print(tc, i, j, bin_code)