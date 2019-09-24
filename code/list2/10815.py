# 숫자카드 10815.py

n = int(input())
my = list(map(int, input().split()))
m = int(input())
your_cards = list(map(int, input().split()))
my = sorted(my)

result = []

for your in your_cards:
    # 이진 탐색
    right = n - 1
    left = 0
    mid = (left + right) >> 1
    while left <= right:
        if your > my[mid]:
            left = mid + 1
        elif your < my[mid]:
            right = mid - 1
        else:
            # 탐색성공
            result.append('1')
            break
        mid = (left + right) >> 1
    else:
        if your == my[mid]:
            result.append('1')
        else:
            result.append('0')
print(' '.join(result))
