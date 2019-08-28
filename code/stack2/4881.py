# 4881.py 배열 최소 합
import sys
sys.stdin = open('4881input.txt', 'r')

def min_sum(tmp, i): # tmp: 배열합, i: 행
    global result

    if i == n:
        result = min(tmp, result)
        return

    if tmp >= result:
        return

    for j in range(n):
        if not used[j]:
            used[j] = True
            min_sum(tmp + my_map[i][j], i + 1)
            used[j] = False

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    my_map = [list(map(int, input().split())) for _ in range(n)]

    result = 10 * n # 답, 들어갈 수 있는 수 3 ~ 10

    used = [False] * n # used[j]: j열 선택 유무
    min_sum(0, 0)
    print('#{} {}'.format(tc, result))



