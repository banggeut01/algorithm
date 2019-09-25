# 4012_fail.py 요리사
# 제한시간 초과!!
import copy
import sys
sys.stdin = open('4012input.txt', 'r')

def get_synergy(choosed):
    tmp = 0
    for i in range(len(choosed) - 1):
        for j in range(i + 1, len(choosed)):
            tmp += ingrd[choosed[i]][choosed[j]] # i, j가 식재료일 때 시너지
            tmp += ingrd[choosed[j]][choosed[i]]
    return tmp

def get_other(g1):
    g2 = []
    for i in range(N): # 식재료 중에서
        if i not in g1: # 그룹1에 뽑히지 않은 원소
            g2.append(i)
    return g2

def comb(k, s): # k:k번째원소뽑기, s:시작인덱스
    if k == M:
        if cur not in comb_list:
            copied = copy.deepcopy(cur) # 이과정 안하면, comb_list에 들어간 후 값 계속 수정됨
            comb_list.append(copied) # 그룹1
            comb_list.append(get_other(copied)) # 그룹2
        return

    for i in range(s, N):
        cur.append(i)
        comb(k + 1, i + 1)
        cur.pop()

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    ingrd = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2
    cur = [] # 그룹1 식재료 조합
    MIN = 20000 * N * N
    comb_list = []
    comb(0, 0) # 조합 리스트 comb_list 구하기
    for x in range(len(comb_list) // 2):
        s1 = get_synergy(comb_list[x * 2])
        s2 = get_synergy(comb_list[x * 2 + 1])
        MIN = min(MIN, abs(s1 - s2))
    print('#{} {}'.format(tc, MIN))
