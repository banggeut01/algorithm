# 4012_fail.py 요리사
import sys
sys.stdin = open('4012input.txt', 'r')

def get_synergy(choosed, i):
    tmp = 0
    for e in choosed: # 현재까지 뽑힌 원소들
        tmp += ingrd[e][i] # x, i가 식재료일 때 시너지
        tmp += ingrd[i][e]
    return tmp

def get_other(g1):
    other = []
    sng = 0
    for i in range(N): # 식재료 중에서
        if i not in g1: # 그룹1에 뽑히지 않은 원소
            other.append(i)
            sng += get_synergy(other, i)
    return sng


def comb(k, s, total): # k:k번째원소뽑기, s:시작인덱스, total:시너지
    global MIN

    if k == M:
        other_sng = get_other(cur)
        d = abs(other_sng - total)
        MIN = min(MIN, d)
        return

    for i in range(s, N):
        tmp = get_synergy(cur, i)
        cur.append(i)
        comb(k + 1, s + 1, total + tmp)
        cur.pop()

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    ingrd = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2
    cur = [] # 식재료 조합
    MIN = 20000 * N * N
    comb(0, 0, 0)
    print('#{} {}'.format(tc, MIN))