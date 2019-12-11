# 17825.py 주사위 윷놀이

def back(k, total):
    global END
    if END == 4 or k == 10:
        global MAX
        MAX = max(MAX, total)
        print(pos)
        return
    
    for x in range(4): # 4개의 말
        if isEnd[x]: continue
        ori0, ori1 = new0, new1 = pos[x][0], pos[x][1]
        diff = new1 + li[k]
        while new0 != -1 and len(score[new0]) < diff:
            diff -= (len(score[new0]) - new1 + 1)
            new0, new1 = dct[new0][1], 0
        if new0 == -1: # 도착인 경우
            oriScore = score[ori0][ori1]
            END += 1
            isEnd[x] = True
            visit[oriScore] = False
            pos[x] = (-1, -1)
            back(k + 1, total)
            END -= 1
            isEnd[x] = False
            visit[oriScore] = True
            pos[x] = (ori0, ori1)
        else: # 도착 아닌 경우
            if len(score[new0]) == diff:
                new0, new1 = dct[new0][0], 0
            else:
                new0, new1 = dct[new0][1], diff
            newScore, oriScore = score[new0][new1], score[ori0][ori1]
            if not visit[newScore]: # 말 없는 경우
                visit[oriScore] = False
                visit[newScore] = True
                pos[x] = (new0, new1)
                back(k + 1, total + newScore)
                visit[oriScore] = True
                visit[newScore] = False
                pos[x] = (ori0, ori1)

score = [[0, 2, 4, 6, 8, 10],                           # 0 -> 1 or 2
        [10, 12, 14, 16, 18, 20],                       # 1 -> 3 or 4
        [10, 13, 16, 19, 25, 26, 27, 28, 30],           # 2 -> 6 or 7
        [20, 22, 24, 25, 30, 35, 40],                   # 3 -> end
        [20, 22, 24, 26, 28, 30],                       # 4 -> 6, 7
        [30, 28, 27, 26, 25, 30, 35, 40],               # 5 -> end
        [30, 32, 34, 36, 38, 40]]                       # 6 -> end

dct = { 0: (2, 1),
        1: (3, 4),
        2: (5, 6),
        3: (-1, -1),
        4: (5, 6),
        5: (-1, -1),
        6: (-1, -1)}

# 주사위 번호 리스트 1~5의 값
li = list(map(int, input().split())) # 길이 10
# 말 4개 - 4개 모두 도착지점이면 끝내버리기
END = 0
MAX = 0
isEnd = [0] * 4 # 말 도착 유무
visit = [0] * 41 # score 말 유무
# 말 1~4 차례대로 움직이기 -> back
# 이미 말이 도착인 경우 더이상 이동할 수 없음
# 이동하려고 하는 칸에 말이 이미 있는 경우 이동할 수 없음!
# 이동할 때마다 점수 추가!
pos = [(0, 0) for _ in range(4)] # 말 4개의 위치 [2][3]이면 19에 있다.
back(0, 0)
print(MAX)