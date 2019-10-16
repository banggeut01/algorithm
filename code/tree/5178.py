# 5178.py 노드의 합

def SumLeaf(x): # x: 노드번호
    if L[x] == 0 and R[x] == 0: # 단말노드
        return V[x]
    return SumLeaf(L[x]) + SumLeaf(R[x])
t = int(input())
for tc in range(1, t + 1):
    N, M, leaf = map(int, input().split()) # N: 노드개수, M: 리프노드개수, L: 출력 노드번호
    # 트리 높이
    H = 1
    while True:
        if N <= 2 ** H - 1:
            break
        H += 1
    L = [0] * (2 ** H)
    R = [0] * (2 ** H)
    V = [0] * (2 ** H)
    # N개 노드 완전이진트리
    for x in range(1, 2 ** (H - 1)):
        if x * 2 <= N:
            L[x] = x * 2
        if x * 2 + 1 <= N:
            R[x] = x * 2 + 1
    # 리프 노드 입력
    for _ in range(M):
        x, val = map(int, input().split()) # 노드번호, 값
        V[x] = val
    result = SumLeaf(leaf)
    print('#{} {}'.format(tc, result))