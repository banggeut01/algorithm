# 2005.py 파스칼의 삼각형

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    print('#{}\n1'.format(tc))
    tmp, cur = [], []
    for i in range(2, N + 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                cur.append(1)
            else:
                cur.append(tmp[j - 1] + tmp[j])
        print(*cur)
        tmp, cur = cur, []
