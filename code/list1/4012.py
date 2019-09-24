# 4012.py 요리사
import copy
# import sys
# sys.stdin = open('4012input.txt', 'r')

def get_synergy(choosed):
    tmp = 0
    for i in range(len(choosed) - 2):
        for j in range(i + 1, len(choosed)):
            tmp += ingrd[i][j] # i, j가 식재료일 때 시너지
            tmp += ingrd[j][i]
    return tmp

def get_other(g1):
    other = []
    for i in range(N): # 식재료 중에서
        if i not in g1: # 그룹1에 뽑히지 않은 원소
            other.append(i)
    return other

def comb(k, s): # k:k번째원소뽑기, s:시작인덱스
    global MIN
    print('#s값은 {}'.format(s))
    if k == M:
        sng1 = get_synergy(cur)
        print(sng1, cur)
        g2 = get_other(cur)
        sng2 = get_synergy(g2)
        print(sng2, g2)
        MIN = min(MIN, abs(sng1 - sng2))
        return

    for i in range(s, N):
        cur.append(i)
        comb(k + 1, s + 1)
        cur.pop()

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    ingrd = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2
    cur = [] # 그룹1 식재료 조합
    MIN = 20000 * N * N
    # comb_list = []
    comb(0, 0)
    print('#{} {}'.format(tc, MIN))