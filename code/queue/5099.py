# 5099.py
# 피자 굽기
import collections

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n: 화덕크기, m: 피자개수
    chz = list(map(int, input().split())) # 치즈 양
    oven = collections.deque() # 화덕
    pizza = collections.deque(num for num in range(m))

    for i in range(n):
        oven.append(pizza.popleft())

    remain = collections.deque()
    if n < m:
        while pizza:
            remain.append(pizza.popleft())

    while len(oven) > 1:
        p = oven.popleft()# 화덕에서 꺼내기
        chz[p] = chz[p] // 2
        if chz[p] == 0: # 치즈 모두 녹음
            if remain:
                oven.append(remain.popleft())
        else: # 치즈 안녹음
            oven.append(p) # 화덕에 다시 넣음

    print('#{} {}'.format(tc, oven.popleft() + 1))



