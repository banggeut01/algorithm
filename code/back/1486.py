# 1486.py 장훈이의 높은 선반
import sys
sys.stdin = open('1486input.txt', 'r')


def back(k, total):
    global ANS
    if ANS == 0:
        return
    if k == N:
        if total >= B:
            ANS = min(total - B, ANS)
        return

    back(k + 1, total + H[k]) # 선택
    back(k + 1, total) # 노선택
t = int(input())
for tc in range(1, t + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ANS = B
    back(0, 0)
    print('#{} {}'.format(tc, ANS))