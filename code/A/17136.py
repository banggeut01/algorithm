# 17136.py 색종이 붙이기

def checkSize(r, c, size):
    if -1 < r + size <= 10 and -1 < c + size <= 10:
        for i in range(r, r + size):
            for j in range(c, c + size):
                if not board[i][j]:
                    return False
        return True
    else:
        return False

def updatePaper(r, c, size, val):
    for i in range(r, r + size):
        for j in range(c, c + size):
            board[i][j] = val

def dfs(r, tmp): # 시작인덱스, tmp:현재색종이개수
    global cnt

    if sum(map(sum, board)) == 0: # cnt 갱신조건
        if cnt == -1:
            cnt = tmp
        else:
            cnt = min(cnt, tmp)
        return

    if tmp >= cnt and cnt != -1: # 가지치기
        return

    for i in range(r, 10):
        for j in range(10):
            if board[i][j]:
                flag = 0
                for size in range(5, 0, -1): # 크기 5부터 붙여봄
                    if checkSize(i, j, size): # 붙이기 가능하면,
                        if paper[size]:
                            flag = 1
                            paper[size] -= 1  # 붙이기
                            updatePaper(i, j, size, 0)
                            dfs(i, tmp + 1)
                            paper[size] += 1# 되돌리기
                            updatePaper(i, j, size, 1)
                if not flag: # 색종이 하나도 못붙이면,
                    return
                return


board = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5] # paper: 색종이 개수, 인덱스: 색종이 크기
cnt = -1
dfs(0, 0) # 시작 행인덱스, 붙인 색종이 개수
print(cnt)

