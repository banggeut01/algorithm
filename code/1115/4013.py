# 4013.py [모의 SW 역량테스트] 특이한 자석
from collections import deque

def rotation(n, d): # n:톱니바퀴번호, d:회전방향 1시계, -1반시계
    visit[n] = True
    signR, signL = gear[n][2], gear[n][6]
    if d == 1: # 시계
        gear[n].appendleft(gear[n].pop())
    else: # 반시계
        gear[n].append(gear[n].popleft())
    if R[n] and gear[R[n]][6] != signR and not visit[R[n]]: rotation(R[n], d * (-1))
    if L[n] and gear[L[n]][2] != signL and not visit[L[n]]: rotation(L[n], d * (-1))

# 왼쪽 오른쪽
R = [0, 2, 3, 4, 0]
L = [0, 0, 1, 2, 3]
for tc in range(1, int(input()) + 1):
    gear = [[0]] # 1~4번 톱니바퀴, 0:N극 1:S극
    K = int(input())
    for i in range(1, 5):
        gear += [deque(map(int, input().split()))]
    for k in range(K):
        n, d = map(int, input().split()) # n:톱니바퀴번호, d:회전 방향
        visit = [False] * 5
        rotation(n, d)
    result = 0
    for x in range(4):
        if gear[x + 1][0]: result += 2 ** x
    print('#{} {}'.format(tc, result))