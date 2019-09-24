#4861chu.py
T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    string = []

    bpoint = 0

    for i in range(N):

        string.append(input())

    for y in range(N):

        for x in range(N - M + 1):

            flag = 0

            for i in range(int(M/2)):

                if string[y][x + i] == string[y][x + M - 1 - i]:

                    flag += 1

                else:

                    break

            if flag == int(M/2):

                strr = ""

                for ans in range(M):

                    strr+=string[y][x+ans]

                print("#"+str(test_case)+" "+strr)

                bpoint = 1

                break;

        if bpoint == 1:

            break

    for y in range(N - M + 1):

        for x in range(N):

            flag = 0

            for i in range(int(M/2)):

                if string[y + i][x] == string[y + M - 1 - i][x]:

                    flag += 1

                else:

                    break

            if flag == int(M/2):

                strr = ""

                for ans in range(M):

                    strr+=string[y+ans][x]

                print("#"+str(test_case)+" "+strr)

                bpoint = 1

                break;

        if bpoint == 1:

            break