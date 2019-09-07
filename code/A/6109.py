# 6109.py 추억의 2048게임

def pushNumbers(job): # 행, 열
    if job == 'up' or job == 'down':
        for j in range(N):
            tmp, prev = [], 0 # tmp: 갱신 열, prev:이전값
            for i in range(S, E + dir, dir):
                if not prev: # 이전값 0
                    if tile[i][j]:
                        prev = tile[i][j]
                else: # 이전값 0이 아님
                    if tile[i][j] == prev: # 이전값과 같음
                        if tile[i][j] != 8:
                            tmp.append(tile[i][j] * 2)
                        prev = 0 # 이전값 초기화
                    else: # 이전값과 같지 않음
                        tmp.append(prev)
                        if tile[i][j]: # 새로운 값 0이 아니면,
                            prev = tile[i][j]
            if prev: # 이전값 0 아니면,
                tmp.append(prev)
            print(tmp)
            
            i = S
            for x in range(len(tmp)):
                print(tmp)
                tile[i][j] = tmp[x]
                i += dir

            for x in range(N - len(tmp)):
                tile[i][j] = 0
                i += dir
        for i in range(N):
            print(*tile[i])
    else:
        for i in range(N):
            tmp, prev = [], 0 # tmp: 갱신 열, prev:이전값
            for j in range(S, E + dir, dir):
                if not tile[i][j]: # 0일 때,
                    if prev: tmp.append(prev)
                else: # 0 아닐 때,
                    if tile[i][j] == prev: # 이전값과 같으면,
                        if tile[i][j] != 8:
                            tmp.append(tile[i][j] * 2)
                        prev == 0
                    else: # 이전값과 같지 않음,
                        if prev: 
                            tmp.append(prev)
                        prev = tile[i][j]
            if prev: # 이전값 0 아니면,
                tmp.append(prev)
            
            j = S
            for x in range(len(tmp)):
                print(i, j, x)
                tile[i][j] = tmp[x]
                j += dir

            for x in range(N - len(tmp)):
                tile[i][j] = 0
                j += dir
    
            
t = int(input())
for tc in range(1, t + 1):
    N, job = input().split()
    N = int(N)
    tile = [list(map(int, input().split())) for _ in range(N)]
    S, E = 0, N - 1  # s:시작열, e:끝열
    
    if job == 'up':
        dir = 1
    elif job == 'down':
        dir = -1
        S, E = E, S
    elif job == 'right':
        dir = -1
        S, E = E, S
    else: # 'left'
        dir = 1
    
    for _ in range(N): # N 번 반복
        pushNumbers(job)
    
    print('#{}'.format(tc))
    for i in range(N):
        print(*tile[i])

                