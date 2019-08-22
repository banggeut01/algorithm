# 부분집합 생성 코드 예제) 교재에서!
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n: 원소의 개수
for i in range(1<<n) : # 1<<n: 부분집합의 개수
    for j in range(n+1): # 원소의 수만큼 비트 비교
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")

    print()