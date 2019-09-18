# 1240.py 단순 2진 암호코드
import sys
sys.stdin = open('1240input.txt', 'r')
# sys.stdin = open('1240-2input.txt', 'r')
def find_code(prev, i, j):
    c = j - 1
    for _ in range(8): # 8자리 암호코드에 대해
        cnt = 1  # 같은 0 또는 1의 개수
        tmp = []
        flag = 0
        while True:
            if prev == board[i][c]: # 이전값 == 현재값
                cnt += 1
            else: # 이전값 != 현재값
                tmp.append(cnt)
                cnt = 1
                prev = board[i][c]
            if len(tmp) == 4: # 4자리로 이뤄진 암호코드
                tmp = list(reversed(tmp))
                if len(code) == 7 and sum(tmp) > 7: # 첫번째 암호코드
                    tmp[0] = 7 - sum(tmp[1:])
                for idx in range(10):
                    if num[idx] == tmp: # 유효한 암호코드
                        code.append(idx)
                        flag = 1
                        break
                else:# 유효하지 않은 암호코드 1, 1, 2, 2
                    return False
            c -= 1
            if flag:
                break
    return True

def is_valid():
    if len(code) == 8: # 8개의 암호코드
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
    else:
        return False

# 암호 번호
num = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
        [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # 행,열 크기
    board = [list(map(int, list(input()))) for _ in range(N)]
    code = []  # 암호코드
    flag = 0
    for i in range(N):
        if sum(board[i]):
            for j in range(M - 1, -1, -1): # 끝에서부터
                if board[i][j]: # 0 아닌 지점 발견시
                    if find_code(1, i, j): # 8자리 암호코드 다 찾았을 때,
                        if is_valid(): # 검증 성공
                            print('#{} {}'.format(tc, sum(code)))
                        else: # 검증 실패
                            print('#{} 0'.format(tc))
                    else: # 잘못된 암호코드 일 때,
                        print('#{} 0'.format(tc))
                    flag = 1
                    break
            if flag:
                break
    # print(code)
