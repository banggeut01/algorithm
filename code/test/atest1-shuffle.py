# test1.py shuffle-O-Matic 2019

import collections
# import sys
# sys.stdin = open('sample_input1.txt', 'r')


def shuffle(snum, x, dcard): # snum:셔플시행횟수, x:다이얼번호, card:카드
    card = dcard[:]
    if snum > 5:
        return -1

    dq = collections.deque()

    if x <= N // 2:
        s1, s2 = N // 2 - x, N // 2
        for idx in range(x):
            dq.append(card[s2 + idx])
            dq.append(card[s1 + idx])

        s1, s2 = N // 2 - x - 1, N // 2 + x
        if -1 < s1 < N and -1 < s2 < N:
            for idx in range(N // 2 - x):
                dq.appendleft(card[s1 - idx])
                dq.append(card[s2 + idx])
    else:
        for idx in range(N // 2):
            dq.appendleft(card[N - 1 - idx])
            dq.append(card[idx])
    flag = False
    if card[0] == 1:
        for i in range(1, N):
            if dq[i] != dq[i - 1] + 1: # 오름차순
                break
        else:
            flag = True
    elif card[0] == N:
        for i in range(1, N):
            if dq[i] != dq[i - 1] - 1: # 내림차순
                break
        else:
            flag = True

    if flag:
        return snum
    else:
        for k in range(1, 5):
            return tmp.append(shuffle(1, k, card))



t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 카드개수
    card = collections.deque(list(map(int, input().split())))

    flag = False
    if card[0] == 1:
        for i in range(1, N):
            if card[i] != card[i - 1] + 1: # 오름차순
                break
        else:
            flag = True
    elif card[0] == N:
        for i in range(1, N):
            if card[i] != card[i - 1] - 1: # 내림차순
                break
        else:
            flag = True
    if not flag:
        tmp = []
        for k in range(1, 5):

            tmp.append(shuffle(1, k, card))
            result = min(tmp)
    else:
        result = 0

    print(result)