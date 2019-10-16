# 5177.py 이진 힙
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    li = list(map(int, input().split()))
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
    top = 1
    for x in li:
        V[top] = x
        c = top # 자식
        p = c // 2 # 부모
        while p > 0 and V[c] < V[p]:
            V[c], V[p] = V[p], V[c]
            c = p
            p = c // 2
        top += 1

    x, total = N // 2, 0
    while x != 0:
        total += V[x]
        x = x // 2

    print('#{} {}'.format(tc, total))