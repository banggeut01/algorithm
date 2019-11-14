# 2105.py [모의 SW 역량테스트] 디저트 카페
import sys
sys.stdin = open('2105input.txt', 'r')
def getCafeCnt(i, j, ur, dr): # ur: 시작점으로부터 우상향 횟수, dr: 시작점으로부터 우하향 횟수
    # ur이 0이면 우상향
    # ur이 0이 아니고, dr 0이면, 우상향 or 우하향
    # dr 0이 아니면 우하향 or (좌하향 => 좌상향) 시작점 돌아오면 개수(ur+dr)*2
    if not ur:
        # 우상향
        if -1 < i - 1 < N and -1 < j + 1 < N and not board[i - 1][j + 1] in cafeList:
            cafeList.append(board[i - 1][j + 1])
            getCafeCnt(i - 1, j + 1, ur + 1, dr)
            cafeList.pop()
        return
    elif not dr:
        # 우상향
        if -1 < i - 1 < N and -1 < j + 1 < N and not board[i - 1][j + 1] in cafeList:
            cafeList.append(board[i - 1][j + 1])
            getCafeCnt(i - 1, j + 1, ur + 1, dr)
            cafeList.pop()
        # 우하향
        if -1 < i + 1 < N and -1 < j + 1 < N and not board[i + 1][j + 1] in cafeList:
            cafeList.append(board[i + 1][j + 1])
            getCafeCnt(i + 1, j + 1, ur, dr + 1)
            cafeList.pop()
        return
    else:
        # 우하향
        if -1 < i + 1 < N and -1 < j + 1 < N and not board[i + 1][j + 1] in cafeList:
            cafeList.append(board[i + 1][j + 1])
            getCafeCnt(i + 1, j + 1, ur, dr + 1)
            cafeList.pop()
        # 좌하향(ur만큼) 후 좌상향(dr만큼)
        tmp = 0
        x = 0
        while x < ur: # 좌하향
            if -1 < i + 1 < N and -1 < j - 1 < N and not board[i + 1][j - 1] in cafeList:
                cafeList.append(board[i + 1][j - 1])
                i, j = i + 1, j - 1
                tmp += 1
                x += 1
            else:
                while tmp > 0:
                    cafeList.pop()
                    tmp -= 1
                return
        x = 0
        while x < dr: # 좌상향
            if -1 < i - 1 < N and -1 < j - 1 < N and not board[i - 1][j - 1] in cafeList:
                cafeList.append(board[i - 1][j - 1])
                i, j = i - 1, j - 1
                tmp += 1
                x += 1
            else:
                while tmp > 0:
                    cafeList.pop()
                    tmp -= 1
                return
        # 시작점으로 돌아옴
        global MAX
        if MAX == -1: MAX = (ur + dr) * 2
        else: MAX = max(MAX, (ur + dr) * 2)
        while tmp > 0:
            cafeList.pop()
            tmp -= 1
        return
            


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * 101 # 인덱스:디저트번호 
    cafeList = [] # 방문 카페
    MAX = -1 # 답
    for i in range(1, N - 1):
        for j in range(N - 2):
            cnt = getCafeCnt(i, j, 0, 0)
    print('#{} {}'.format(tc, MAX))
