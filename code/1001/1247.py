# 1247.py 최적 경로
# 회사 -> 고객 모두 방문 -> 집
import sys
sys.stdin = open('1247input.txt', 'r')

def back(i, j, k, d): # 좌표, 고객수, 거리
    global MIN
    if d >= MIN:
        return
    if k == N:
        d = d + abs(point[2] - i) + abs(point[3] - j)
        MIN = min(MIN, d)
        return
    for x in range(N):
        if not visit[x]:
            r, c = point[x*2 + 4], point[x*2 + 5]
            visit[x] = True
            back(r, c, k + 1, d + abs(i-r) + abs(j-c))
            visit[x] = False

t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 고객
    point = list(map(int, input().split())) # 0~1:회사,2~3:집,4~:고객
    visit = [False] * N
    MIN = 0xffffff
    i, j = point[0], point[1]
    back(i, j, 0, 0)
    print('#{} {}'.format(tc, MIN))