# 16637.py 괄호 추가하기 fail
import copy

def calcul(n1, n2, w): # n1,n2숫자, o연산자
    if w == '+': return n1 + n2
    elif w == '*': return n1 * n2
    else: return n1 - n2

def perm(k):
    if k == M:
        global MAX
    # seq = [1, 2, 0]
        n = copy.deepcopy(nums) # 숫자 값 리스트 복사본
        o = copy.deepcopy(seq) # 연산자 인덱스 순열 복사본
        word = []
        for i in range(len(o)):
            word.append(oprt[o[i]])
        while o:
            w = word.pop(0)
            idx = o.pop(0)
            n2 = n.pop(idx + 1)
            n1 = n.pop(idx)
            n.insert(idx, calcul(n1, n2, w))
            for i in range(len(o)):
                if o[i] >= idx: o[i] -= 1
        MAX = max(MAX, n[0])
        return

    for x in range(M):
        if not used[x]:
            seq.append(x)
            used[x] = True
            perm(k + 1)
            seq.pop()
            used[x] = False

N = int(input())
li = list(input())
nums, oprt = [], []
for x in range(N):
    if not x % 2: nums.append(int(li[x]))
    else: oprt.append(li[x])
M = len(oprt) # 연산자 개수
seq = [] # 연산자 순열
used = [False] * M
MAX = 0
parent = [n for n in range(len(nums))] # 부모
perm(0)
print(MAX)

