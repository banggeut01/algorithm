# 종이붙이기 4869.py

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return paper(n-1) + paper(n-2) * 2


t = int(input())
for tc in range(1, t + 1):
    length = int(input())

    result = paper(length//10)
    print('#{} {}'.format(tc, result))


