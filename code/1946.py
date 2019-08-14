# 간단한 압축 풀기 1946.py

t = int(input())
for tc in range(t):
    n = int(input())

    result = []

    for _ in range(n):
        char, num = input().split()
        num = int(num)
        result += char*num

    print('#{}'.format(tc+1))
    while len(result) > 10:
        print(''.join(result[:10]))
        result = result[10:]

    print(''.join(result))