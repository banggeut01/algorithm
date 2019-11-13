# 2661. 좋은 수열(백트래킹)

def isGood(seq):
    e = len(seq) # 비교 시작점
    maxM = e // 2
    for m in range(2, maxM + 1): # 패턴길이 m
        if seq[e-m:e] == seq[e-m*2:e-m]:
            return False
    return True

def back(k):
    global seq, MIN, FLAG
    if FLAG: return

    if k == N:
        MIN = min(MIN, int(''.join(seq)))
        FLAG = 1
        return

    for i in range(1, 4):
        if seq and seq[-1] == str(i): continue
        seq.append(str(i))
        if isGood(seq):
            back(k + 1)
        seq.pop()

N = int(input())
MIN = 10 ** 80
seq = []
FLAG = 0
back(0)
print(MIN)