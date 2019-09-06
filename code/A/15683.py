# 15683.py 감시
import pprint
def backtrack(r, tmp, zero):
    global result, cctvNum

    if tmp == cctvNum:
        result = min(zero, result)

        pprint.pprint(board)
        print(zero)

        return

    for i in range(r, N):
        for j in range(M):
            if not board[i][j]: continue
            if board[i][j] != 6 and board[i][j] != '#' and not used[i][j]: # 카메라 찾음!
                s = board[i][j] # cctv 상태 1 ~ 5
                for case in cctv[s]:
                    visit = []  # 방문좌표 임시저장
                    for direct in case:
                        dx, dy = d[direct]
                        row, col = i + dx, j + dy
                        while -1 < row < N and -1 < col < N and board[row][col] != 6:
                            if not board[row][col] and board[row][col] != '#':
                                visit.append((row, col))
                                zero -= 1
                                board[row][col] = '#'
                            row, col = row + dx, col + dy
                    used[i][j] = True
                    backtrack(i, tmp + 1, zero)
                    for row, col in visit:# 되돌리기
                        board[row][col] = 0
                        zero += 1
                    used[i][j] = False
                return


# N, M = map(int, input().split()) # N:행, M:열
# board = [list(map(int, input().split())) for _ in range(N)]
N, M = 6, 6
board = [[0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 0, 0],
 [0, 0, 0, 0, 6, 0],
 [0, 6, 0, 0, 2, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 5]]
d = [(0, -1), (0, 1), (1, 0), (0, -1)] # [0]:상, [1]:우, [2]:하, [3]:좌
cctv = [[],  # [0]
        [[0], [1], [2], [3]],  # [1] 4가지
        [[0, 2], [1, 3]],  # [2] 2가지
        [[0, 1], [1, 2], [2, 3], [3, 0]],  # [3] 4가지
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # [4] 4가지
        [[0, 1, 2, 3]]]  # [5] 1가지
cctvNum, result = 0, N * M
zero = 0
used = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            zero += 1
            continue
        if board[i][j] != 6: cctvNum += 1
pprint.pprint(board)
backtrack(0, 0, zero) # 시작행, 감시완료한 cctv개수, 0개수
print(result)

