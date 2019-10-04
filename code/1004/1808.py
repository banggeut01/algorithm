# 1808. 지희의 고장난 계산기

def isPossible(x): # 계산기 눌리는지
    b = 0 # button
    while x > 9:
        if not visit[x % 10]: return -1
        x = x // 10
        b += 1
    if not visit[x]: return -1
    else: return b + 1

def calcul(x, tmp): # x: 숫자, tmp: 횟수
    if not visit[i]:
        b = isPossible(x)
        if b != -1:
            global ANS
            tmp += b
            ANS = min(ANS, tmp)
    else:

t = int(input())
for tc in range(1, t + 1):
    inputs = list(map(int, input().split()))
    N = int(input())
    visit = [False] * (N + 1)
    cnt = [0] * (N + 1)
    ANS = 0xffffff
    for i in inputs:
        if i:
            visit[i] = True
            cnt[i] = 1
    calcul(N, 1)