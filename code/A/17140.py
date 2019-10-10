# 17140.py 이차원 배열과 연산

TR, TC, TV = map(int, input().split())
TR, TC = TR - 1, TC - 1
board = [[0] * 100 for _ in range(100)] # 3*3
for i in range(3):
    IN = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = IN[j]
N, M = 3, 3
result = 0
while board[TR][TC] != TV:
    if result == 100:
        result = -1
        break
    if N >= M:
        # 행정렬
        for i in range(N):
            # 하나의 행에 대하여 복사 tmp = [1, 1, 2]
            tmp = []
            for j in range(M):
                tmp.append(board[i][j])
            tmp = sorted(tmp)
            ntmp = [] # 값, 개수 ntmp = [1, 2, 2, 1]
            prev = 0
            for x in tmp:
                if x != prev:
                    prev = x
                    ntmp.append(x)
                    ntmp.append(tmp.count(x))
            # 선택정렬
            for a in range(0, len(ntmp), 2):
                # a 최소값 올 자리
                idx, minCnt, minVal = a, ntmp[a + 1], ntmp[a]
                for b in range(a + 2, len(ntmp), 2):
                    if ntmp[b + 1] < minCnt: # 개수
                        minCnt, minVal = ntmp[b + 1], ntmp[b]
                        idx = b
                    elif ntmp[b + 1] == minCnt:
                        if ntmp[b] < minVal:
                            minVal = ntmp[b]
                            idx = b
                ntmp[a], ntmp[idx] = ntmp[idx], ntmp[a]
                ntmp[a + 1], ntmp[idx + 1] = ntmp[idx + 1], ntmp[a + 1]

            M = max(M, len(ntmp))
            M = min(M, 100)
            for x in range(len(ntmp)):
                board[i][x] = ntmp[x]
            for x in range(len(ntmp), M):
                board[i][x] = 0
    else:
        # 열정렬
        for j in range(M):
            # 하나의 열에 대하여 복사 tmp = [1, 1, 2]
            tmp = []
            for i in range(N):
                tmp.append(board[i][j])
            tmp = sorted(tmp)
            ntmp = [] # 값, 개수 ntmp = [1, 2, 2, 1]
            prev = 0
            for x in tmp:
                if x != prev:
                    prev = x
                    ntmp.append(x)
                    ntmp.append(tmp.count(x))
            # 선택정렬
            for a in range(0, len(ntmp), 2):
                # a 최소값 올 자리
                idx, minCnt, minVal = a, ntmp[a + 1], ntmp[a]
                for b in range(a + 2, len(ntmp), 2):
                    if ntmp[b + 1] < minCnt: # 개수
                        minCnt, minVal = ntmp[b + 1], ntmp[b]
                        idx = b
                    elif ntmp[b + 1] == minCnt:
                        if ntmp[b] < minVal:
                            minVal = ntmp[b]
                            idx = b
                ntmp[a], ntmp[idx] = ntmp[idx], ntmp[a]
                ntmp[a + 1], ntmp[idx + 1] = ntmp[idx + 1], ntmp[a + 1]
            N = max(N, len(ntmp))
            N = min(N, 100)
            for x in range(len(ntmp)):
                board[x][j] = ntmp[x]
            for x in range(len(ntmp), M):
                board[x][j] = 0
    result += 1
print(result)


