# 전기버스
import sys
sys.stdin = open('4831input.txt', 'r')

t = int(input())
for tc in range(t):
    # k:최대 이동 정류장수, n:이동해야하는 총 정류장수, m:충전기 설치된 정류장 수
    k, n, m = map(int, input().split())
    if k*m < n:
        print('#{} {}'.format(tc+1, 0))
    else:
        values = list(map(int, input().split()))
        station = [0]*n # 정류장
        for value in values:
            station[value] = 1 # 충전기가 있는 정류장
        cnt = 0 # 충전 횟수
        pos = 0 # 현재 위치
        while pos < n-k:
            for j in range(k, 0, -1): # 갈 수 있는 거리 내에서 충전기 탐색
                if station[pos+j]: # 최근 충전기 찾으면
                    cnt += 1
                    pos += j
                    break
            # 충전기 찾지 못하면
            else:
                pos = n
                cnt = 0
        if cnt > m:  # 최대 충전기 개수 넘으면,
            cnt = 0
        print('#{} {}'.format(tc+1, cnt))


