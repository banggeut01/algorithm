# 5186.py 이진수2
t = int(input())
for tc in range(1, t + 1):
    num = float(input())
    result = []
    cnt = 0
    while num != 0:
        num = num * 2
        if num >= 1:
            result.append(1)
        else:
            result.append(0)
        num = num - num // 1
        cnt += 1
        if cnt > 12:
            print('#{} overflow'.format(tc))
            break
    else:
        print('#{} {}'.format(tc, ''.join(list(map(str, result)))))
