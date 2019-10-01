# 1244.py 최대 상금
import sys
sys.stdin = open('1244input.txt', 'r')
def getNum():
    val = ''
    for i in range(M):
        val += NUM[i]
    return int(val)

def switch(k): # k번째 교환
    global MAX
    if k == N:
        tmp = getNum()
        MAX = max(MAX, tmp)
        return

    for i in range(M - 1):
        for j in range(i + 1, M):
            NUM[i], NUM[j] = NUM[j], NUM[i]
            tmp = getNum()
            if not visit[k][tmp]:
                visit[k][tmp] = True
                switch(k + 1)
            NUM[i], NUM[j] = NUM[j], NUM[i]

t = int(input())
for tc in range(1, t + 1):
    inputs, N = input().split()
    NUM = list(inputs)
    N = int(N) # 교환횟수
    M = len(NUM) # 숫자길이
    MAX = 0
    visit = [[False] * 1000000 for _ in range(N)]
    switch(0)
    print('#{} {}'.format(tc, MAX))