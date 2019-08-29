# 2597.py 줄자접기
# 빨 -> 파 -> 노
# 접어서 더 큰 것



n = int(input())
l, r = 0, n
dots = []
for _ in range(3):
    input1, input2 = map(float, input().split())
    dots.append([min(input1, input2), max(input1, input2)])

check = [False] * 3
i = 0
while i < 3:
    if not check[i]:
        mid = (dots[i][0] + dots[i][1]) / 2

        for j in range(i + 1, 3):
            if not check[j] and (dots[j][0] + dots[j][1]) / 2 == mid: # 같은 곳에서 접히면
                check[j] = True
            else: # 점 이동
                if mid - l > r - mid: # 점을 왼쪽 자로 이동
                    if dots[j][0] > mid: # 점 오른쪽에 있으면,
                        dots[j][0] = mid - (dots[j][0] - mid)
                    if dots[j][1] > mid:
                        dots[j][1] = mid - (dots[j][1] - mid)
                    dots[j][0], dots[j][1] = min(dots[j][0], dots[j][1]), max(dots[j][0], dots[j][1])
                else: # 오른쪽으로 이동
                    if dots[j][0] < mid: # 점 왼쪽에 있으면,
                        dots[j][0] = mid + (mid - dots[j][0])
                    if dots[j][1] < mid:
                        dots[j][1] = mid + (mid - dots[j][1])
                        # tmp = mid + (mid - dots[j][1])
                        # dots[j][0], dots[j][1] = min(dots[j][0], tmp), max(dots[j][0], tmp)
                    dots[j][0], dots[j][1] = min(dots[j][0], dots[j][1]), max(dots[j][0], dots[j][1])

        # 자르기
        if mid - l > r - mid:
            r = mid
            result = mid - l
        else:
            l = mid
            result = r - mid

    # print(dots, result, i)
    i += 1
print('{0:.1f}'.format(result))

