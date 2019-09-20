# 5189.py 전기카트


def back(k, prev, usage): # k 이동횟수, idx:이전 구역, usage:사용량
    global MIN

    if usage > MIN:
        return

    if k == N - 1:
        MIN = min(MIN, usage + battery[prev][0])
        return

    for i in range(1, N):
        if not visit[i]:
            visit[i] = True
            back(k + 1, i, usage + battery[prev][i])
            visit[i] = False

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    MIN = N * N * 100
    back(0, 0, 0)
    print('#{} {}'.format(tc, MIN))