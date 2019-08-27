# 4875.py 미로
import sys
sys.stdin = open('4875input.txt', 'r')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    my_map = [list(map, input().split()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if my_map == 2:

