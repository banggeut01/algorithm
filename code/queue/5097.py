# 5097.py 회전

import collections

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n: 숫자개수, m: 작업횟수
    jobs = collections.deque(input().split())

    for i in range(m):
        jobs.append(jobs.popleft())


    print('#{} {}'.format(tc, jobs.popleft()))


