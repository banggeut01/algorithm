# 1244_fail.py 최대 상금
# 시간 초과
def switch(k): # k번째 교환
    global MAX
    if k == N:
        val, e = 0, M - 1
        for i in range(M):
            val += NUM[i] * (10**e)
            e -= 1
        MAX = max(MAX, val)
        return

    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            NUM[i], NUM[j] = NUM[j], NUM[i]
            switch(k + 1)
            NUM[i], NUM[j] = NUM[j], NUM[i]

t = int(input())
for tc in range(1, t + 1):
    inputs, N = input().split()
    NUM = list(map(int, inputs))
    N = int(N)
    M = len(NUM)
    MAX = 0
    switch(0)
    print('#{} {}'.format(tc, MAX))