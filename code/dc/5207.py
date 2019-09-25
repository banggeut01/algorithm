# 5207.py 이진 탐색


def binarySearch(lo, hi, key):
    global cnt
    state = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < A[mid]:
            if state == 1: break
            state = 1
            hi = mid - 1
        elif key > A[mid]:
            if state == 2: break
            state = 2
            lo = mid + 1
        else:
            return True
    return False

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    cnt = 0
    for i in range(M):
        if binarySearch(0, N - 1, B[i]): cnt += 1
    print('#{} {}'.format(tc, cnt))