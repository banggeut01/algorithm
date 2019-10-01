# 2115.py 벌꿀채취

# 1. 두명의 일꾼, 각 일꾼 가로로 연속되도록 M개의 벌통 선택

# 2. 하나의 벌통 -> 하나의 용기에 담아야 함
#    한 일꾼당 최대 꿀의 양 C를 넘을 수 없음
#    모두 채취 or 노 채취

# 3. 채취한 꿀, 각각의 제곱만큼 수익
import sys
sys.stdin = open('2115input.txt', 'r')
def getHoney(r, c): # rc좌표에서 최대 수익
    maxVal = 0
    for i in range(1 << M):
        tmp, total = 0, 0
        for j in range(M):
            if i & (1 << j):
                total += board[r][c + j]
                tmp += board[r][c + j] ** 2
        if total < C:
            maxVal = max(maxVal, tmp)
    return maxVal

def selectArea(r, c, total):
    global MAX
    for i in range(r, N):
        for j in range(N - M + 1):
            if i == r: # 현재 위치 다음부터 시작한다.
                if j < c + M:
                    continue
            if j - c < M:
                continue
            if MAX < total + H[i][j]:
                print(r, c, i, j)
            MAX = max(MAX, total + H[i][j])



t = int(input())
for tc in range(1, t + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    H = [[0] * (N - M + 1) for _ in range(N)]
    MAX = 0
    for i in range(N):
        for j in range(N - M + 1):
            H[i][j] = getHoney(i, j)
    print(H)
    for i in range(N):
        for j in range(N - M + 1):
            selectArea(i, j, H[i][j])
    # print(MAX)
