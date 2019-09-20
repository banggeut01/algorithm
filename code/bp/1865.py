# 1865.py 동철이의 일 분배

def assign_work(k, p): # k:k번째 직원, p:성공확률
    global result

    if p < result:
        return

    if k == N:
        result = max(result, p)
        return

    for j in range(N):
        if not used[j] and stats[k][j] > 0:
            used[j] = True
            assign_work(k + 1, p * stats[k][j])
            used[j] = False

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    stats = [list(map(int, input().split())) for _ in range(N)] # 행:직원, 열:작업, 값:능력치
    for i in range(N):
        for j in range(N):
            stats[i][j] = stats[i][j] / 100
    used = [False] * N # 작업 할당 여부
    result = 0
    assign_work(0, 1)
    print('#{} {:.6f}'.format(tc, result*100))