# 5209.py 최소 생산 비용

def back(k, total): # k번째 제품의 공장을 선택
    global MIN
    if k == N:
        MIN = min(MIN, total)
        return
    if total > MIN:
        return
    for j in range(N):
        if not used[j]:
            used[j] = True
            back(k + 1, total + cost[k][j])
            used[j] = False

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)] # i행:제품, j열:공장
    MIN = N * 99
    used = [False] * N
    back(0, 0)
    print('#{} {}'.format(tc, MIN))
