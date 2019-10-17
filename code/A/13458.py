# 13458.py 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
total = 0
for x in range(len(A)):
    A[x] -= B
    total += 1
    if A[x] > 0:
        total += A[x] // C
        if A[x] % C:
            total += 1
print(total)