# 2578.py 빙고
import sys
sys.stdin = open('2578input.txt', 'r')

# 5 * 5 2차원 리스트
arr = [list(map(int, input().split())) for _ in range(5)]

# 부르는 수
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

check = [0] * 12 # row_cnt:0~4, col_cnt:5~9, cross_cnt:10~11
cnt = 0

for num in nums:
    flag = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                check[i] += 1
                check[5 + j] += 1
                if i == j:
                    check[10] += 1
                if i + j == 4:
                    check[11] += 1
                flag = 1
                cnt += 1
                # print(arr[i][j], i, j, check)
                break # 숫자 arr에서 지워지면 이중 for문 종료, 새 숫자 받기
        if flag:
            break
    bingo = 0
    for chk in check:
        if chk == 5: # 빙고
            bingo += 1
    if bingo >= 3:
        print(cnt)
        break
else:
    print(25)