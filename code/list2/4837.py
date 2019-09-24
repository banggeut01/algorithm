# 부분집합의 합 4837.py
uset = [i for i in range(1, 13)]

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    result = 0 # 답
    for i in range(1 << len(uset)): # 총 부분집합 개수 2^12
        set_sum = 0
        set_cnt = 0
        for j in range(len(uset)): # 집합의 원소 개수만큼
            if i & (1 << j):
                set_sum += uset[j]
                set_cnt += 1
        # 부분집합 생성 완료
        if set_cnt == n and set_sum == k:
            result += 1
    print('#{} {}'.format(tc, result))
