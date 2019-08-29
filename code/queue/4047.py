# 4047.py 영준이의 카드 카운팅

t = int(input())
for tc in range(1, t + 1):
    S = dict()
    D = dict()
    H = dict()
    C = dict()

    card = input()
    for i in range(len(card)//3):
        p, n = card[3 * i], int(card[3 * i + 1:3 * i + 3]) # 모양, 숫자
        if p == 'S':
            if not S.get(n):
                S[n] = 1
            else:
                print('#{} ERROR'.format(tc))
                break
        elif p == 'D':
            if not D.get(n):
                D[n] = 1
            else:
                print('#{} ERROR'.format(tc))
                break
        elif p == 'H':
            if not H.get(n):
                H[n] = 1
            else:
                print('#{} ERROR'.format(tc))
                break
        else: # 'C'
            if not C.get(n):
                C[n] = 1
            else:
                print('#{} ERROR'.format(tc))
                break

    else:
        result = []
        print('#{} {} {} {} {}'.format(tc, 13 - len(S), 13 - len(D), 13 - len(H), 13 - len(C)))