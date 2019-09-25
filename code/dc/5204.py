# 5204.py 병합 정렬
def mergeSort(lo, hi):
    global cnt
    if lo == hi:
        return
    mid = (lo + hi + 1) // 2
    mergeSort(lo, mid - 1)
    mergeSort(mid, hi)
    if a[mid - 1] > a[hi]:
        cnt += 1
    i, j, k = lo, mid, lo
    while i <= mid - 1 and j <= hi:
        if a[i] <= a[j]:
            tmp[k] = a[i]; k, i = k + 1, i + 1
        else:
            tmp[k] = a[j]; k, j = k + 1, j + 1
    while i <= mid - 1:
        tmp[k] = a[i]; k, i = k + 1, i + 1
    while j <= mid:
        tmp[k] = a[j]; k, j = k + 1, j + 1
    for x in range(lo, hi + 1):
        a[x] = tmp[x]

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    a = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    mergeSort(0, N - 1)
    print('#{} {} {}'.format(tc, a[N//2], cnt))