# 6109.py 추억의 2048게임
t = int(input())
for tc in range(1, t + 1):
    N, job = input().split()
    N = int(N)
    tile = [list(map(int, input().split()))]

    tmp = []
    for _ in range(N):
        