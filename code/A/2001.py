# 2001.py 파리 퇴치
import sys
sys.stdin = open('2001input.txt', 'r')

def getFlyCnt(r, c, m):
    cnt = 0

    for i in range(r, r + m):
        for j in range(c, c + m):
           cnt += mymap[i][j]

    return cnt

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n: map크기, m: 파리채크기
    mymap = [list(map(int, input().split())) for _ in range(n)]

    result = 0 # 답
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            result = max(result, getFlyCnt(i, j, m))

    print('#{} {}'.format(tc, result))