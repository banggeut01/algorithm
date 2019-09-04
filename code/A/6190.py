# 6190.py 정곤이의 단조 증가하는 수

def findChoosedIdx():
    for i in range(len(used)):
        if used[i]: # 선택된 원소 발견!
            return i + 1
    return 0 # 선택된 원소 없을 때, 첫번째 원소 선택

def isMono(num):
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True

def chooseEle(k, tmp): # k선택된 원소개수, tmp:선택원소들의 곱
    global result

    if k == 2: # 두개의 원소 선택되면,
        if result < tmp and isMono(str(tmp)):
            result = tmp
        return

    idx = findChoosedIdx()
    for i in range(idx, n):
        used[i] = True # i원소 선택
        chooseEle(k + 1, tmp * ele[i])
        used[i] = False
    return

t = int(input())
for tc in range(1, t + 1):
    n = int(input()) # 원소 개수
    ele = list(map(int, input().split())) # 원소
    used = [False] * n # n개원소에 대한 선택 유무

    result = -1 # 답
    chooseEle(0, 1)
    print('#{} {}'.format(tc, result))