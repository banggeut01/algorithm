# 2578.py 빙고
import sys
sys.stdin = open('2578input.txt', 'r')

# 5 * 5 2차원 리스트
arr = [list(map(int, input().split())) for _ in range(5)]

# 부르는 수
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

# 지워진 개수를 값으로 갖는 리스트
# 5개 행(idx 0 ~ 4), 5개 열, 우하향 대각선 1개, 좌하향 대각선 1개
check_list = [0] * 12
line_cnt = 0 # 그어진 선의 개수
num_cnt = 0

for num in nums:
    for row in range(5):
        for col in range(5):
            if arr[row][col] == num:
                # 행
                check_list[row] += 1
                if check_list[row] == 5: # 빙고면,
                    line_cnt += 1 # 그어진 선 개수 ++1

                # 열
                check_list[4 + col] += 1
                if check_list[4 + col] == 5:
                    line_cnt += 1

                # 우하향 대각선
                if row == col:
                    check_list[10] += 1
                    if check_list[10] == 5:
                        line_cnt += 1

                # 좌하향 대각선
                elif row + col == 5:
                    check_list[11] += 1
                    if check_list[11] == 5:
                        line_cnt += 1
                num_cnt += 1
                if line_cnt == 3:  # 지워진 선 3개면,
                    print(num_cnt)
                    sys.exit(1)
                break
