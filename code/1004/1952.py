# 1952.py 수영장

import sys
sys.stdin = open('1952input.txt', 'r')

def dfs(k, cost): # k달, 현재까지 비용
    global MIN
    if k > 11:
        MIN = min(MIN, cost)
    if cost >= MIN:
        return
    if T[2] < triC[k]:
        dfs(k + 3, cost + T[2]) # 3달 선택
    dfs(k + 1, cost + C[k]) # 노선택
t = int(input())
for tc in range(1, t + 1):
    T = list(map(int, input().split())) # 티켓 비용(1일, 1달, 3달, 1년)
    D = list(map(int, input().split())) # 각달 이용일수, 0-11달
    C = [0] * 14  # 각 달 비용
    triC = [0] * 12 # 3달 비용(idx=2면, 2-4달 비용)
    MIN = 3000 * 31 * 12
    for i in range(12):
        C[i] = D[i] * T[0] # 1일
        C[i] = min(C[i], T[1]) # 1달
    # 3달
    for i in range(12):
        triC[i] = sum(C[i:i+3])
    used = [0] * 12
    dfs(0, 0) # 3달
    MIN = min(MIN, T[3]) # 1년
    print('#{} {}'.format(tc, MIN))



