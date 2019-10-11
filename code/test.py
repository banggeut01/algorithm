# 연소ㅐ행렬곱생
def matrix(start, end):
    if start == end : return 0
    MIN = 0xffffff
    for k in range(start, end + 1):
        left = matrix(start, k)
        right = matrix(k + 1, end)
        if MIN > left + right + row[start]*col[k]*col[end]
            MIN = left + right + row[start]*col[k]*(col[end])
        dp[start][end] = MIN
        return MIN
            