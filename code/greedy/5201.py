# 5201.py 컨테이너 운반

def load_ctn(k, total): # k번째 컨테이너, total:총무게
    global MAX

    # if k == END: # 선택된 컨테이너가 N개, 또는 M개이면
    #     MAX = max(MAX, total)
    #     return

    MAX = max(MAX, total)
    for i in range(M): # M개 트럭에 대해,
        print(k, i)
        if not used[i] and W[k] <= T[i]: # 쓰이지않은, 가능한 트럭
            used[i] = True # 선택
            # print('i{} T[i]{} k{} W[k]{} total{}'.format(i, T[i], k, W[k], total+W[k]))
            load_ctn(k + 1, total + W[k])
            used[i] = False # 취소

# t = int(input())
t = 1
for tc in range(1, t + 1):
    # N, M = map(int, input().split()) # N-컨테이너수, M-트럭수
    # W = list(map(int, input().split())) # 화물 무게
    # T = list(map(int, input().split())) # 트럭 적재용량
    N, M = 3, 2
    # END = min(3, 2)
    W = [1, 5, 3]
    T = [8, 3]
    used = [False] * M
    MAX = 0
    load_ctn(0, 0)
    print(MAX)