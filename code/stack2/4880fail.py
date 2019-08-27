# 4880fail.py 토너먼트 카드게임
# 재귀로 풀어보자
# 이렇게 짜면 안된다!

def tnamt(n, now): # n:학생번호, now:현재트리높이
    if height == now: # height: 완전이진트리 높이
        if n <= N: # N: 전체학생수
            return n
        else:
            return 0

    l = tnamt(2 * n - 1, now + 1) # 왼쪽 학생 번호
    r = tnamt(2 * n, now + 1) # 오른쪽 학생 번호
    g1, g2 = rps[l - 1], rps[r - 1] # 왼/오 학생의 가위바위보

    if g1 == 1: # 가위
        if g2 == 1 or g2 == 0 or g2 == 3: # 무승부 or 이긴 경우
            return l # 왼쪽 학생 번호
        else: # r == 2
            return r # 오른쪽 학생 번호
    elif g1 == 2: # 바위
        if g2 == 2 or g2 == 0 or g2 == 1:
            return l
        else:
            return r
    elif g1 == 3: # 보
        if g2 == 3 or g2 == 0 or g2 == 2:
            return l
        else:
            return r
    else: # 0
        return r


t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 학생수
    rps = list(map(int, input().split()))

    height = 1 # 트리 높이
    while N > 1 << height:
        height += 1

    result = tnamt(1, 0) # 1:학생번호, 0:현재트리높이
    print('#{} {}'.format(tc, result))