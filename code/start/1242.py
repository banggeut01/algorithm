# 1242.py 암호코드 스캔

import sys
sys.stdin = open('1242input.txt', 'r')

def scan_code(i):
    global j

    # 초기 str_bin : 뒤에서부터 0자름 ex) 0100이면 01
    str_bin = bin(int('0x' + board[i][j], 16)) # 16진수->2진수
    str_bin = str_bin[2:] # '0x100' -> '100'
    str_bin = '0'*(4-len(str_bin)) + str_bin # '100' -> '0100'
    str_bin = str_bin.rstrip('0') # '0100' -> '01'
    tmp = [] # 0 또는 1의 길이 저장할 리스트
    prev, cnt = '1', 0

    # 첫번째 str_bin에 대해
    for idx in range(len(str_bin) - 1, -1, -1):
        if prev == str_bin[idx]:  # 이전값 == 현재값
            cnt += 1
        else:  # 이전값 != 현재값
            tmp.append(cnt)
            prev = str_bin[idx]
            cnt = 1
    j = j - 1
    flag = 0

    while len(code) < 9: # 8자리의 암호코드 찾을 동안 (못찾는 경우 빠져나오지 못함, 만약 암호코드가 7자리만 나온다면,,?) 이런 경우는 없긴 할듯
        if j < 0: # 이거 안하면 runtime error!
            return False
        str_bin = bin(int('0x' + board[i][j], 16))  # 16진수->2진수
        str_bin = str_bin[2:]
        str_bin = '0' * (4 - len(str_bin)) + str_bin

        for idx in range(3, -1, -1): # ex) str_bin = '1101'
            if prev == str_bin[idx]: # 이전값 == 현재값
                cnt += 1
            else: # 이전값 != 현재값
                tmp.append(cnt)
                prev = str_bin[idx]
                cnt = 1

            if len(code) == 7 and len(tmp) == 3: # 마지막 암호코드 일 때,
                for x in range(3):
                    tmp[x] = tmp[x] // length
                tmp.append(7-sum(tmp))
                tmp = tuple(reversed(tmp))  # 리버스 후 튜플로 변환
                c = element.get(tmp)  # 한자리의 암호코드를 찾는다.
                if c != None:  # 유효한 암호코드일 때,
                    code.append(c)
                else:  # 유효하지 않은 암호코드일 때,
                    return False
                j = j - 1
                return True

            elif len(tmp) == 4: # 4개의 구성요소 찾으면, (마지막암호코드 아닐 때)
                if not flag:
                    length = min(tmp)
                    for x in range(4):
                        tmp[x] = tmp[x] // length
                    flag = 1
                else:
                    for x in range(4):
                        tmp[x] = tmp[x] // length
                tmp = tuple(reversed(tmp))
                c = element.get(tmp)
                if c != None:
                    code.append(c)
                else:
                    return False
                tmp = [] # 4개 구성요소 리스트 초기화
        j = j - 1
    return True

def is_valid():
    total = 0
    for i in range(8):
        if i % 2: # 홀수자리,
            total += code[i] * 3
        else:
            total += code[i]
    if not total % 10:
        return True
    else:
        return False

# 암호코드 구성요소
element = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,
                (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # 행,열 크기
    board = [list(input()) for _ in range(N)]
    code = []  # 암호코드
    result = 0 # 답
    for i in range(N):
        for j in range(M - 1, 13, -1): # 열의 끝에서부터,
            if board[i][j] != '0' and -1 < i - 1 and board[i - 1][j] == '0': # 0이 아닌 곳 찾음
                if scan_code(i): # 암호코드 8자리 스캔
                    if is_valid(): # 검증 성공했을 때,
                        result += sum(code) # 답갱신
                code = [] # 암호코드 초기화
    print('#{} {}'.format(tc, result))