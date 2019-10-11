# 1232.py 사칙연산


def calcul(w):  # V = 현재 노드
    if str(V[w]).isdigit(): return V[w]
    if V[w] == '*': return calcul(L[w]) * calcul(R[w])
    elif V[w] == '+': return calcul(L[w]) + calcul(R[w])
    elif V[w] == '/': return calcul(L[w]) / calcul(R[w])
    elif V[w] == '-': return calcul(L[w]) - calcul(R[w])



for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    V = [0] * (N + 1)
    for _ in range(N):
        li = list(input().split())
        n, v= int(li[0]), li[1]
        if v.isdigit():
            v = int(v)
        else: # 연산자
            l, r = int(li[2]), int(li[3])
            L[n] = l
            R[n] = r
        V[n] = v # 값
    result = calcul(1)
    print('#{} {}'.format(tc, int(result)))
