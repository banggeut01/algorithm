# 구간합
import sys
sys.stdin = open('4835input.txt', 'r')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    tmp = 0
    for j in range(m):
         tmp += num[0 + j]
    max_num = min_num = tmp    # 최대, 최소 초기값

    for i in range(1, n-m+1): # n-m번
        tmp = 0
        for j in range(m):
            tmp += num[i+j]
        if tmp > max_num:
            max_num = tmp
        elif tmp < min_num:
            min_num = tmp
    print('#{} {}'.format(tc+1, max_num-min_num))
