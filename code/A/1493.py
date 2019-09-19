# 1493.py 수의 새로운 연산

def get_idx(p):
    # 행 번호 찾기
    n, tmp = 1, 0
    while True:
        tmp += n
        if tmp >= p:
            break
        n += 1
    # 열 번호 찾기
    i, j = n, 0
    for _ in range(n):
        if tmp == p:
            return (i, j)
        else:
            i, j = i - 1, j + 1
            tmp -= 1

def get_num(i, j):
    r, c = i, j
    # 몇번째 줄에 있는지
    while True:
        if r == 0:
            break
        r, c = r - 1, c + 1
    # r - 1줄에 위치함
    # 열 찾기
    tmp = 0
    for n in range(1, r):
        tmp += n
    for _ in range(n):
        if tmp
t = int(input())
for tc in range(1, t + 1):
    p, q = map(int, input().split())
    px, py = get_idx(p) # &(p) 인덱스 반환
    qx, qy = get_idx(q)
    get_num(px + qx, py + qy) # #(i, j) 숫자 반환


    # print('#{} {}'.format(tc, result))
