# 1697_fail.py 숨바꼭질

N, K = map(int, input().split()) # N:현재숫자, K:목표숫자
N, K = min(N, K), max(N, K)
cur, to = ['1'], list(bin(K - N).replace('0b', ''))

cnt = 0 # 답
for i in range(1, len(to)):
    if to[i] == '1': # *2, + 1 => 연산 2번
        cur.append('1')
        cnt += 2
    else:
        cur.append('0') # *2 => 연산 1번
        cnt += 1

print(cnt)