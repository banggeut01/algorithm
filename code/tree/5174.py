# 5174.py subtree

def order(v): # V = 현재 노드
    if v == 0: return
    global result
    result += 1
    order(L[v])
    order(R[v])

t = int(input())
for tc in range(1, t + 1):
    E, N = map(int, input().split()) # 간선, 노드번호
    li = list(map(int, input().split()))
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    for x in range(E):
        p, c = li[x * 2], li[x * 2 + 1]
        if L[p]: R[p] = c
        else: L[p] = c
    result = 0
    order(N)
    print('#{} {}'.format(tc, result))