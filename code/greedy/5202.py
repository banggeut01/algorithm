# 5202.py 화물 도크

def get_work_cnt(k, cnt, prev): # k번째 작업, 몇대, 마지막 작업시각
    global MAX
    if k == N:
        MAX = max(MAX, cnt)
        return

    get_work_cnt(k + 1, cnt, prev) # 노선택
    if prev <= work[k][0]: # 선택
        get_work_cnt(k + 1, cnt + 1, work[k][1])

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    work = []
    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))
    work = sorted(work)
    MAX = 0
    get_work_cnt(0, 0, 0)
    print('#{} {}'.format(tc, MAX))