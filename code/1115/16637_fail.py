# 16637_fail.py 괄호 추가하기
import copy
def findParent(idx, p):
    if p[idx] != idx:
        return findParent(p[idx], p)
    return idx

def calcul(n1, n2, o): # n1,n2숫자, o연산자
    if o == '+': return n1 + n2
    elif o == '*': return n1 * n2
    else: return n1 - n2

def perm(k):
    # if k == M:
    global MAX
    seq = [1, 2, 0]
    num = copy.deepcopy(nums)
    p = copy.deepcopy(parent)
    for idx in range(M):
        if p[seq[idx]] != seq[idx]: numIdx = findParent(seq[idx], p) # 피연산자1 인덱스
        else: numIdx = seq[idx]
        rtn = calcul(num[numIdx], num[seq[idx] + 1], oprt[seq[idx]])
        p[seq[idx] + 1] = numIdx
        num[numIdx] = rtn
    if MAX < rtn: print(p);print(num);print(seq)
    MAX = max(MAX, rtn)
    return
    #
    # for x in range(M):
    #     if not used[x]:
    #         seq.append(x)
    #         used[x] = True
    #         perm(k + 1)
    #         seq.pop()
    #         used[x] = False

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

