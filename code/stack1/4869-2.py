# 종이붙이기 4869-2.py
# DP로 해보기

memo = [-1] * 30
def paper(n):
    memo[0], memo[1] = 1, 3

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2] * 2

    return memo[i]


    return 1 + paper(n)

t = int(input())
for tc in range(1, t + 1):
    length = int(input())

    result = paper(length//10)
    print('#{} {}'.format(tc, result))
