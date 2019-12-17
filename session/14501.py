# 14501.py 퇴사
# 0 ~ N - 1, N일 퇴사
N = int(input())
T, P = [], [] # T:기간, P:이익
D = [0] * (N + 1)
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
for x in range(N):
    D[x + 1] = max(D[x + 1], D[x])
    if x + T[x] <= N:
        D[x + T[x]]  = max(D[x + T[x]], D[x] + P[x])
print(D[N])