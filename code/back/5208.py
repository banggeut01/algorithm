# 5208.py 전기버스2

def back(pos, cnt): # pos:현재위치, cnt:교체횟수
    global MIN
    if pos >= N:
        MIN = min(MIN, cnt)
        return
    if cnt > MIN:
        return
    d = battery[pos] # 최대 갈 수 있는 거리
    for i in range(d, 0, -1):
        back(pos + i, cnt + 1)

t = int(input())
for tc in range(1, t + 1):
    battery = list(map(int, input().split())) # [0] = N, [1]~[N - 1]: N-1개
    N = battery[0]
    MIN = battery[0] - 1
    back(1, -1)
    print('#{} {}'.format(tc, MIN))