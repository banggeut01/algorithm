# 14501.py 퇴사
def backtrack(idx, price): # idx: 현재날짜, p:이득
    global result
    
    if idx == N:
        result = max(result, price)
        return

    if T[idx] <= N - idx: # 선택가능하면,
        backtrack(idx + T[idx], price + P[idx]) # 선택
    backtrack(idx + 1, price) # 노선택

N = int(input())
T, P = [], []
result = 0

for _ in range(N):
    task, price = map(int, input().split())
    T.append(task)
    P.append(price)
backtrack(0, 0)
print(result)
