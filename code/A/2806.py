# 2806.py N-Queen

import sys
sys.stdin = open('2806.txt', 'r')

def isPromising(r, c): # 유망검사할 행,열 위치
    for idx in range(r): # r-1 행까지
        if col[idx] == c: # idx:행,col[idx]:열, 같은 열이면
            return False
        if abs(r - idx) == abs(c - col[idx]): # 대각선이면,
            return False

    return True

def nqueen(k): # k행에서 queen 놓는 함수
    global result, n

    if k == n: # n-1행까지 queen 놓았음
        result += 1
        return
    
    for j in range(n):
        if isPromising(k, j): # 유망하면,
            col[k] = j
            nqueen(k + 1)
            col[k] = False

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    result = 0 # 답
    
    col = [False] * n # col[i] : i행에 놓인 queen의 열
    nqueen(0) # 행
    print('#{} {}'.format(tc, result))
