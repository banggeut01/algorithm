T = int(input())


def square_sum(x, y, k):
    result = 0
    for i in range(x, x + k):
        for j in range(y, y + k):
            if i == x or i == x + k - 1:
                result += com[i][j]
            else:
                if j == y or j == y + k - 1:
                    result += com[i][j]

    return result


for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    com = [list(map(int, input().split())) for _ in range(N)]

    max_N = 0

    for i in range(N - K + 1):
        for j in range(M - K + 1):
            max_N = max(max_N, square_sum(i, j, K))

    print('#{} {}'.format(t, max_N))
