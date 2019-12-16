# 14889_teacher.py 스타트와 링크
# 알쌤 풀이
N = 4
def backtrack(k, acnt, bcnt):
    if acnt > N // 2 or bcnt > N // 2: return
    if acnt == N // 2 and bcnt == N // 2:
        pass # 시너지를 구함

    # k번 값을 A에 추가할지
    A[acnt] = k
    backtrack(k + 1, acnt + 1, bcnt)
    # B에 추가할지
    B[bcnt] = k
    backtrack(k + 1, acnt, bcnt + 1)

A = [0] * N
B = [0] * N

backtrack(1, 1, 0)