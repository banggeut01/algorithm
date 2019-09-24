# Flatten
import sys
sys.stdin = open('1208input.txt', 'r')

for tc in range(10):
    n = int(input()) # 덤프 횟수
    box = list(map(int, input().split())) # 상자의 높이값
    # print(box)
    for _ in range(n): # n번 평탄화
        max_idx = min_idx = 0  # 최고점, 최저점 초기화
        for i in range(1, 100): # idx : 1 ~ n-1
            if box[i] > box[max_idx]: # 최고점 갱신
                max_idx = i
            elif box[i] < box[min_idx]: # 최저점 갱신
                min_idx = i
        # 평탄화
        box[max_idx] -= 1
        box[min_idx] += 1

    max_idx = min_idx = 0  # 최고점, 최저점 초기화
    for i in range(1, 100):  # idx : 1 ~ n-1
        if box[i] > box[max_idx]:  # 최고점 갱신
            max_idx = i
        elif box[i] < box[min_idx]:  # 최저점 갱신
            min_idx = i
    print('#{} {}'.format(tc + 1, box[max_idx] - box[min_idx]))
