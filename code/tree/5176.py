# 5176.py 이진탐색
def order(v, k):
    global result
    if k == H - 1: # 단말노드
        V[v] =
    order(L[v])
    order(R[v])

t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 노드수
    H = 1
    while True:
        if N <= 2 ** H - 1:
            break
        H += 1
    V = [0] * (2 ** H)
    order(1, 0)
    print('#{} {}'.format(tc, result))