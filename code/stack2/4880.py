# 4880.py 토너먼트 카드게임
# 재귀로 풀어보자
# 분할정복

def tnamt(s, e): # s: 그룹 첫번째 학생 번호, e: 마지막 학생 번호
    if s == e:
        return s

    num1 = tnamt(s, (s + e) // 2) # 그룹1
    num2 = tnamt((s + e) // 2 + 1, e) # 그룹2
    g1, g2 = rps[num1 - 1], rps[num2 - 1] # 왼/오 학생의 가위바위보

    if g1 == 1: # 가위
        if g2 == 1 or g2 == 3: # 무승부 or 이긴 경우
            return num1 # 왼쪽 학생 번호
        else: # r == 2
            return num2 # 오른쪽 학생 번호
    elif g1 == 2: # 바위
        if g2 == 2 or g2 == 1:
            return num1
        else:
            return num2
    else: # 보
        if g2 == 3 or g2 == 2:
            return num1
        else:
            return num2



t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 학생수
    rps = list(map(int, input().split()))

    height = 1 # 트리 높이
    while N > 1 << height:
        height += 1

    start, end = 1, N
    result = tnamt(start, end)
    print('#{} {}'.format(tc, result))