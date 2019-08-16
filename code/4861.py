# 회문 4861.py
import sys

def row_palin(i, j, m):
    # m: 회문길이, p: 회문idx
    p = 0
    for p in range(p < m // 2):
        if word[i][j + p] == word[i][j + m - p - 1]:
            p += 1
        else:
            return False
    return True

def col_palin(j, i, m):
    p = 0
    for p in range(p < m // 2):
        if word[j + p][i] == word[j + m - p - 1][i]:
            p += 1
        else:
            return False
    return True


sys.stdin = open('4861input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, (input().split())) # n: 문자판 길이, m: 회문 길이
    word = [input() for _ in range(n)] # n*n 문자판
    for i in range(n):
        for j in range(n - m + 1): # 0 ~ n - m
            if row_palin(i, j, m): # 가로회문 찾으면,
                result = []
                for p in range(m):
                    result.append(word[i][j+p])
                print(i, j)
                break
            elif col_palin(j, i, m): # 세로회문 찾으면
                result = []
                for p in range(m):
                    result.append(word[j+p][i])
                print(i, j)
                break
        print('for문 계속 돌아간다.')
    print('#{} {}'.format(tc, ''.join(result)))
        
