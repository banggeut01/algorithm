# 5356.py 의석이의 세로로 말해요.
import sys
sys.stdin = open('5356input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    board = [] # 칠판
    max_len = 0 # 제일 긴 길이
    len_list = [0] * 5 # 5문자열 길이 저장

    for x in range(5):
        tmp = list(input())
        board.append(tmp)
        max_len = max(max_len, len(tmp))
        len_list[x] = len(tmp)

    print('#{} '.format(tc), end='')
    cur_idx = 0 # 현재 출력 위치
    while cur_idx < max_len:
        for x in range(5): # 5 문자열에 대해
            if cur_idx < len_list[x]: # 각 문자열 길이보다 작은 idx일때
                print(board[x][cur_idx], end='') # 출력
        cur_idx += 1
    print()