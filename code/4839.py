# 이진탐색 4839.py

# 중간 페이지 c= int((l+r)/2)로 계산

t = int(input())
for tc in range(1, t+1):
    # p: 책의 전체 쪽 수, pa: A가 찾을 쪽 번호, pb: B가 찾을 쪽 번호
    p, pa, pb = map(int, input().split())
    acnt = bcnt = 0

    left = 1
    right = p
    while left < right:
        mid = (left + right) >> 1
        acnt += 1
        if mid == pa:  # 탐색 성공
            break
        elif mid > pa: # 찾으려는 수 mid 왼쪽에 있을 때
            right = mid
        else: # mid 오른쪽에 있을 때
            left = mid
    else: # 탐색 실패
        acnt = 0

    left = 1
    right = p
    while left < right:
        mid = (left + right) >> 1
        bcnt += 1
        if mid == pb:  # 탐색 성공
            break
        elif mid > pb: # 찾으려는 수 mid 왼쪽에 있을 때
            right = mid
        else: # mid 오른쪽에 있을 때
            left = mid
    else: # 탐색 실패
        bcnt = 0

    if acnt < bcnt:
        win = 'A'
    elif acnt > bcnt:
        win = 'B'
    else:
        win = 0
    print('#{} {}'.format(tc, win))


