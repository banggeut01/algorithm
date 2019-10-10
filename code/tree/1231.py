# 1231. 중위순회
def order(v): # V = 현재 노드
    if v == 0: return
    order(L[v])
    result.append(A[v])
    order(R[v])

for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    A = [0] * (N + 1)
    for v in range(1, N + 1):
        ip = list(input().split())
        A[v] = ip[1]
        if len(ip) >= 3:
            L[v] = int(ip[2])
        if len(ip) == 4:
            R[v] = int(ip[3])
    result = []
    order(1)
    print('#{} {}'.format(tc, ''.join(result)))