# 숫자카드 10815.py

n = int(input())
my_cards = list(map(int, input().split()))
m = int(input())
your_cards = list(map(int, input().split()))
my_cards = sorted(my_cards)

result = []

for your in your_cards:
    # 이진 탐색
    right = len(my_cards) - 1
    left = 0
    for my in my_cards:

        mid = (left + right) >> 1
        print(mid)
        while left != right:
            if your > my[mid]:
                left = mid
            elif your < my[mid]:
                right = mid
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
