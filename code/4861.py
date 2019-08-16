# 회문 4861.py
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, (input().split())) # n: 문자판 길이, m: 회문 길이
    word = [input() for _ in range(n)] # n*n 문자판
    for i in range(n):
        for j in range(n - m + 1):
