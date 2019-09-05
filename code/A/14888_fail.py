# 14888_fail.py 연산자 끼워넣기
import copy

def calculate(j) : # j:연산자 리스트
    global minNum, maxNum

    result = num[0]
    for idx in range(len(j)):
        if j[idx] == '+':
            result += num[idx + 1]
        if j[idx] == '-':
            result -= num[idx + 1]
        if j[idx] == '*':
            result *= num[idx + 1]
        if j[idx] == '//':
            if result >= 0:
                result //= num[idx + 1]
            else:
                result *= -1
                result //= num[idx + 1]
                result *= -1

    minNum, maxNum = min(minNum, result), max(maxNum, result)

def comb(k, j): # k:선택된 원소 개수, j:선택 원소
    tmp = copy.deepcopy(j)
    if k == len(job):
        if tmp not in combedJob:
            combedJob.append(tmp)
            return

    for idx in range(len(job)):
        if not used[idx]:
            tmp.append(job[idx])
            used[idx] = True
            comb(k + 1, tmp)
            tmp.pop()
            used[idx] = False

N = int(input())
num = list(map(int, input().split())) # 피연산자
oprt = list(map(int, input().split())) # 연산자개수
job, combedJob = [], []
if oprt[0]:
    for _ in range(oprt[0]):
        job.append('+')
if oprt[1]:
    for _ in range(oprt[1]):
        job.append('-')
if oprt[2]:
    for _ in range(oprt[2]):
        job.append('*')
if oprt[3]:
    for _ in range(oprt[3]):
        job.append('//')
maxNum, minNum = -0xffffff, 0xffffff
used = [False] * len(job)
comb(0, [])
for j in combedJob:
    calculate(j)
print(maxNum)
print(minNum)