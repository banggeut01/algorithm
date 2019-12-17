# 14888.py 연산자 끼워넣기
def comb(k, total):
    if k == N:
        global MAX, MIN
        MAX, MIN = max(MAX, total), min(MIN, total)
        return

    for x in range(4):
        if O[x]:
            O[x] -= 1
            if x == 0: comb(k + 1, total + A[k])
            elif x == 1: comb(k + 1, total - A[k])
            elif x == 2: comb(k + 1, total * A[k])
            else:
                comb(k + 1, int(total / A[k]))
            O[x] += 1

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split())) # +, -, x, /
MAX, MIN = -1000000000, 1000000000
comb(1, A[0])
print(MAX)
print(MIN)