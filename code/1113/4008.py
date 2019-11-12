# 4008.py [모의 SW 역량테스트] 숫자 만들기
import sys
sys.stdin = open('4008input.txt', 'r')
def perm(k, total):
    if k == N:
        global MIN, MAX
        MIN = min(MIN, total)
        MAX = max(MAX, total)
        return

    for x in range(4): # 0:+, 1:-, 2:*, 3://
        if cnt[x] > 0:
            cnt[x] -= 1
            if x == 0: perm(k + 1, total + nums[k])
            elif x == 1: perm(k + 1, total - nums[k])
            elif x == 2: perm(k + 1, total * nums[k])
            else:
                if total < 0: perm(k + 1, total * (-1) // nums[k] * (-1))
                else: perm(k + 1, total // nums[k])
            cnt[x] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 숫자 개수
    cnt = list(map(int, input().split())) # 연산자 개수 +, -, *, /
    nums = list(map(int, input().split())) # 수식에 사용되는 숫자 N개
    MIN, MAX = 100000000, -100000000
    perm(1, nums[0])
    print('#{} {}'.format(tc, MAX - MIN))