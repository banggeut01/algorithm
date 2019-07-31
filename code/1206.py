# View
# import sys
# sys.stdin = open('1206input.txt', 'r')

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2): # N-4번
        if arr[i] > arr[i-1] and arr[i] > arr[i-2]: # 왼쪽 검사
            # tmp1 = min(arr[i] - arr[i-1], arr[i] - arr[i-2])
            tmp1 = arr[i] - arr[i-2] if arr[i]-arr[i-1] > arr[i] - arr[i-2] else arr[i]-arr[i-1]
            if arr[i] > arr[i+1] and arr[i] > arr[i+2]: # 오른쪽 검사
                # tmp2 = min(arr[i] - arr[i+1], arr[i] - arr[i+2])
                tmp2 = arr[i] - arr[i+2] if arr[i] - arr[i+1] > arr[i] - arr[i+2] else arr[i] - arr[i+1]
                if tmp1 > tmp2:
                    cnt += tmp2
                else:
                    cnt += tmp1
                # cnt += min(tmp1, tmp2)
    print('#{} {}'.format(tc + 1, cnt))