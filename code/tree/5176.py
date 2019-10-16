# 5176.py 이진탐색

def order(x):
    global val
    if x == 0:
        return
    order(L[x])
    V[x] = val
    val += 1
    order(R[x])

t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 노드수
    H = 1
    while True:
        if N <= 2 ** H - 1:
            break
        H += 1
    L = [0] * (2 ** H)
    R = [0] * (2 ** H)
    V = [0] * (2 ** H)
    for x in range(1, 2 ** (H - 1)):
        if x * 2 <= N:
            L[x] = x * 2
        if x * 2 + 1 <= N:
            R[x] = x * 2 + 1
    val = 1
    order(1)
    print('#{} {} {}'.format(tc, V[1], V[N // 2]))