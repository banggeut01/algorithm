# 부분집합의 합 4837-2.py
# 백트래킹으로 풀어보기
# 가지치기 해보기

def subset(k, n, cnt, tmpsum): # cnt = 현재 선택한 원소수, tmp_sum: 원소들 합
    global result, ele_cnt, setsum
    if tmpsum > setsum:
        return
    if k == n:
        if tmpsum == setsum and cnt == ele_cnt:
            result += 1
        return
    subset(k + 1, n, cnt + 1, tmpsum + uset[k]) # 왼쪽(1:포함)
    subset(k + 1, n, cnt, tmpsum) # 오른쪽(0:미포함)

# 배열은 객체라서 괜찮지만, int형 같은 경우 인자로 넘겨 사용해야함! by, 준영.
uset = [i for i in range(1, 13)]
t = int(input())
for tc in range(1, t+1):
    ele_cnt, setsum = map(int, input().split())

    result = 0
    subset(0, 12, 0, 0)


    print('#{} {}'.format(tc, result))
