import copy, collections

def bfs(end): # end:도착점 리스트
    global result
    total = 0 # 총 치킨거리
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    for r, c in start: # 각 시작점에 대해
        visit = [[False] * N for _ in range(N)]
        dq = collections.deque()
        dq.append((r, c)) # 시작점 방문
        visit[r][c] = True

        flag = 0
        while dq:
            i, j = dq.popleft()
            for idx in range(4): # 4방향에 대해
                row, col = i + x[idx], j + y[idx]
                if 0 <= row < N and 0 <= col < N and not visit[row][col]:
                    if mymap[row][col] == 2 and (row, col) in end: # 도착점 찾음!
                        # 치킨 거리 구하기 - 집(r,c) 치킨(row,col)
                        distance = abs(r - row) + abs(c - col)
                        total += distance
                        flag = 1
                        break
                    visit[row][col] = True
                    dq.append((row, col))
            if flag:
                break
    result = min(result, total)


def chooseEnd(idx, cur): # idx:선택시작점, cur:선택된치킨집 리스트
    tmp = copy.deepcopy(cur)
    if len(tmp) == M:
        endlist.append(tmp)
        return

    for i in range(idx, len(chicken)):
        tmp.append(chicken[i])
        chooseEnd(i + 1, tmp)
        tmp.pop()

N, M = map(int, (input().split())) # N:도시크기, M:치킨집개수
# 1: 집, 2: 치킨집
mymap = [list(map(int, input().split())) for _ in range(N)]
start, chicken = [], [] # start: 집, chicken: 치킨집
endlist = []
result = 0xffffff
for i in range(N):
    for j in range(N):
        if mymap[i][j] == 1: # 집
            start.append((i, j))
        elif mymap[i][j] == 2: # 치킨집
            chicken.append((i, j))

chooseEnd(0, [])
for i in range(len(endlist)):
    bfs(endlist[i])
print(result)