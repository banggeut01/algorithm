# 5201.py 컨테이너 운반

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split()) # N-컨테이너수, M-트럭수
    W = list(map(int, input().split())) # 화물 무게
    T = list(map(int, input().split())) # 트럭 적재용량
    MAX = 0
    W, T  = sorted(W), sorted(T)
    wi, ti = N - 1, M - 1
    while -1 < wi and -1 < ti:
        if W[wi] <= T[ti]: # 적재
            MAX += W[wi]
            ti -= 1
        wi -= 1
    print('#{} {}'.format(tc, MAX))