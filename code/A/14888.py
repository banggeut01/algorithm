# 14888.py 연산자 끼워넣기
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
    if k == N - 1:
        job.append(tmp)
        return

    for idx in range(4):
        if oprtNum[idx]: # 연산자 개수 남아있을 때,
            tmp.append(oprt[idx])
            oprtNum[idx] -= 1
            comb(k + 1, tmp)
            tmp.pop()
            oprtNum[idx] += 1

N = int(input())
num = list(map(int, input().split())) # 피연산자
oprtNum = list(map(int, input().split())) # 연산자개수
job = []
oprt = ['+', '-', '*', '//']
maxNum, minNum = -1000000000, 1000000000
comb(0, [])
for j in job:
    calculate(j)
print(maxNum)
print(minNum)