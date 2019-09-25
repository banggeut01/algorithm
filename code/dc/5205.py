#5205.py 퀵 정렬

def quickSort(lo, hi):
    if lo >= hi: return

    i, j = lo, hi
    while i <= j:
        while i <= hi and a[i] <= a[lo]: i += 1
        while a[j] > a[lo]: j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[lo], a[j] = a[j], a[lo]
    quickSort(lo, j - 1)
    quickSort(j + 1, hi)

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    a = list(map(int, input().split()))
    quickSort(0, N - 1)
    print('#{} {}'.format(tc, a[N//2]))