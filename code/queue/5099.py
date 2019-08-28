# 5099.py
# 피자 굽기
import collections

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n: 화덕크기, m: 피자개수
    chz = list(map(int, input().split())) # 치즈 양
    oven = collections.deque() # 화덕
    pizza = [num + 1 for num in range(m)]

    for i in range(n):
        oven.append(pizza[i])

    if n < m:
        remain = []
        for i in range(n - m + 1, m + 1):
            remain.append(pizza[i])

    print(oven, remain)

    while len(pizza) > 1:
        p = pizza.popleft() # 화덕에서 꺼내기
        chz[p] = chz[p] // 2
        if chz[p] == 0: # 치즈 모두 녹음
            a = 1


