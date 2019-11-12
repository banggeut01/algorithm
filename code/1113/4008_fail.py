def perm(k):
    if k == N - 1:
        total = nums[0]
        for x in range(N - 1):
            if oprt[x] == 0:
                total += nums[x + 1]
            elif oprt[x] == 1:
                total -= nums[x + 1]
            elif oprt[x] == 2:
                total *= nums[x + 1]
            else:
                total //= nums[x + 1]
                if total < 0: total += 1
        result.append(total)
        return

    for x in range(4):  # 0:+, 1:-, 2:*, 3://
        if cnt[x] > 0:
            cnt[x] -= 1
            oprt.append(x)
            perm(k + 1)
            cnt[x] += 1
            oprt.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 숫자 개수
    cnt = list(map(int, input().split()))  # 연산자 개수 +, -, *, /
    nums = list(map(int, input().split()))  # 수식에 사용되는 숫자 N개
    oprt = []  # N - 1개
    result = []
    perm(0)
    print('#{} {}'.format(tc, max(result) - min(result)))