# 5208.py 전기버스2
'''
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
'''

# 풀이 아래를 인자로 교체 or 노교체
# 1. 현재 정류장 번호
# 2. 충전지 잔량
# 3. 충전횟수

def path(cur, elec, cnt): # 정류장번호, 충전량, 교체횟수
    global ans
    if cnt >= ans: return
    if cur >= arr[0]:
        ans = cnt
    else:
        if elec > 0:
            path(cur + 1, elec - 1, cnt) # 노교체
        path(cur + 1, arr[cur] - 1, cnt + 1) # 교체

t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split())) # [0] = N, [1]~[N - 1]: N-1개
    ans = arr[0]
    path(1, arr[1], 0)
    print('#{} {}'.format(tc, ans))