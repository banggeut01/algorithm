# 숫자 카드
import sys
sys.stdin = open('4834input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    numbers = input()

    cnt = [0]*10 # 0~9 개수 저장할 리스트
    for num in numbers:
        cnt[int(num)] += 1

    max_cnt = cnt[0]
    max_num = 0
    for i in range(1, 10):
        if cnt[i] >= max_cnt: # 더 개수가 크면
            max_cnt = cnt[i]
            max_num = i
    print('#{} {} {}'.format(tc+1, max_num, max_cnt))
