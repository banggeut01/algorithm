# 1242best.py 선생님 풀이 암호코드 스캔
P = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3,
     (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
     (2, 1, 3): 8, (1, 1, 2): 9}
A = ord('A')
nine, zero = ord('9'), ord('0')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    def getVal(ch):
        t = ord(ch)
        val = (t - A) + 10 if t > nine else t - zero
        return val


    def find():
        ret = 0
        for i in range(N):
            j = M - 1
            while j >= 0:
                if arr[i][j] != '0' and arr[i - 1][j] == '0':
                    pwd = []
                    L = MIN = 0
                    val, c = getVal(arr[i][j]), 0
                    for k in range(8):
                        c2 = c3 = c4 = 0
                        while (val & 1) == 0:
                            val, c = val >> 1, c + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while val & 1:
                            val, c, c4 = val >> 1, c + 1, c4 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while (val & 1) == 0:
                            val, c, c3 = val >> 1, c + 1, c3 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while val & 1:
                            val, c, c2 = val >> 1, c + 1, c2 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        if k == 0:
                            MIN = min(c2, c3, c4)

                        pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])

                    a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if ((b * 3 + a) % 10) == 0:
                        ret += (a + b)
                j -= 1
        return ret


    # --------------------------------------
    print('#{} {}'.format(tc, find()))