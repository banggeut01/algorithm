# 자기 방으로 돌아가기 4408.py
t = int(input())

# 경로 개수 저장
for tc in range(1, t + 1):
    n = int(input())
    route = [0]*200

    for _ in range(n):
        start, end = map(int, input().split())
        # 오른쪽에서 왼쪽으로 가는 경우 고려
        start, end = min(start, end), max(start, end)
        start, end = (start+1)//2-1, (end+1)//2-1

        for i in range(start, end+1):
            route[i] += 1

    max_route = 0
    for r in route:
        if r > max_route:
            max_route = r

    #
    # print(route)
    print('#{} {}'.format(tc, max_route))

