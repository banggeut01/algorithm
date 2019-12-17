# 15686.py 치킨배달
# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리 : 모든 집의 치킨거리 합
def getSet(k, s):
    if k == M:
        global MIN
        sumDist = 0
        for j in range(H):
            tmp = 100 # i번 치킨집 - j번 집 치킨거리
            for i in selected:
                tmp = min(tmp, dist[i][j])
            sumDist += tmp
            if sumDist >= MIN: return
        MIN = sumDist
        return

    for idx in range(s, C):
        selected[k] = idx
        getSet(k + 1, idx + 1)

chicken = []
home = []
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
selected = [0] * M # 선택된 치킨집
MIN = 0xffffff
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: home.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
C, H = len(chicken), len(home)
dist = [[] for _ in range(C)] # 치킨집(행) - 집(열) 거리 리스트
for i in range(C):
    x1, y1 = chicken[i]
    for j in range(H):
        x2, y2 = home[j]
        dist[i].append(abs(x1 - x2) + abs(y1 - y2))
getSet(0, 0)
print(MIN)