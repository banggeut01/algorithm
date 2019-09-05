# 15686.py 치킨 배달

import copy, collections

def getDistance(end): # end:도착점 리스트
    global result
    total = 0 # 총 치킨거리
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    for sr, sc in start: # 각 시작점에서
        distance = 0xffffff # 각 시작점에 대한 치킨거리 최소값
        for gr, gc in end: # 각 도착점에 대해 거리 구하기
            tmp = abs(gr - sr) + abs(gc - sc)
            distance = min(distance, tmp)
        total += distance
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
for i in range(len(endlist)): # 모든 도착점 리스트
    getDistance(endlist[i]) # 한 도착점리스트에 대해, 총 치킨거리 구함
print(result)