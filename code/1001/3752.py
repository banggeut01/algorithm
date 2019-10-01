# 3752.py 가능한 시험 점수

# 정지수 방법
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    visit = [0] * 10001
    visit[0] = 1
    for s in scores:
        # 뒤에서부터 해야 중복 x!
        # 뒤에서부터 해야하는 이유를 알자!
        for i in range(10000, -1, -1):
            if visit[i]:
                visit[i + s] = 1
    print('#{} {}'.format(tc, sum(visit)))
'''
# DFS 백트래킹
def back(k, s): # k: 트리의 높이, 문항번호, s: 지금까지 점수 합
    if visit[k][s]: return
    visit[k][s] = 1
    if k == N:
        global cnt
        cnt += 1
    else:
        back(k + 1, s)             # k번 문제 틀림
        back(k + 1, s + scores[k]) # k번 문제 맞음

t = int(input())
for tc in range(1, t + 1):
    N = int(input()) # 문제<=100
    scores = list(map(int, input().split())) # 배점<=100
    # visit[k][s] : k높이에서의 점수합이 s인 경우가 있으면 True, 없으면 False
    visit = [[False] * (N * 100 + 1) for _ in range(N + 1)]
    cnt = 0
    back(0, 0)
    print('#{} {}'.format(tc, cnt))
'''