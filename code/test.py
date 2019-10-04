import collections
d = [10000, 1000, 100, 10, 1] # 10진수 자리값
def swap(val, i, j):
    a = (val//d[i]) % 10
    b = (val//d[j]) % 10
    # 3 2 8 8 8, 2000 80 교환
    # -2000 +20
    # + 8000 -80
    return val - a * d[i] + a * d[j] - b * d[j] + b * d[i]

num = 32888 # 숫자로
N = len(str(num))
visit = [[0] * 1000000 for _ in range(11)] #
MAX = 0
Q = collections.deque()
Q.append((num, 0))
cnt = 2
while Q:
    val, k = Q.popleft()
    if k == cnt:
        MAX = max(MAX, val)
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                t = swap(val, i, j)
                if visit[k][t]: continue
                Q.append((t, k + 1))

print(MAX)
