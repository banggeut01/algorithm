for t in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))

    num = 0
    for i in range(n-4): # 0 ~ n-5, n-4번
        big = max(arr[i], arr[i+1], arr[i+3], arr[i+4]) # 2~3개는 max 가능
        if arr[i+2] > big:
            num += arr[i+2] - big
    print(f'#{t} {num}')