# 1220.py 마그네틱

import sys
sys.stdin = open('1210input.txt', 'r')

def matnetic(j):


for tc in range(1, 11):
    n = int(input()) # n:테이블크기 n*n테이블
    table = [list(map(int, input().split())) for _ in range(100)]


    end = n - 1
    for col in range(n): # i는 열 번호
        magnetic(col)