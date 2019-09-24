# 특별한 정렬 4843.py
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    for k in range(10): # k는 시작 위치 (10개까지 출력)
        idx = k # 최대값 혹은 최소값 인덱스
        if not k % 2: # k가 짝수번째 인덱스
            for m in range(k+1, n): # (k+1) ~ (n-1)
                if num[m] > num[idx]: # 최대값
                    idx = m

        else: # k가 홀수번째 인덱스
            for m in range(k+1, n):
                if num[m] < num[idx]:  # 최소값
                    idx = m

        num[idx], num[k] = num[k], num[idx] # 최소값 혹은 최대값과 교환

    num = map(str, num[:10])
    print('#{} {}'.format(tc, ' '.join(num)))
