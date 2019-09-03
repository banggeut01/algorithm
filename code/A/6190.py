# 6190.py 정곤이의 단조 증가하는 수

def isMono(num):
    n = num % 10
    while

t = int(input())
for tc in range(1, t + 1):
    n = int(input()) # 원소 개수
    ele = list(map(int, input().split())) # 원소
    result = -1 # 답
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i & 1 << j:
                tmp.append(ele[j])
                if len(tmp) > 2:
                    break
        else:
            if len(tmp) == 2 and result < tmp[0] * tmp[1]:
                if isMono(tmp[0] * tmp[1]):
                    result = tmp[0] * tmp[1]

    print('#{} {}'.format(tc, result))
