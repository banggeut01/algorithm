# 4366.py 정식이의 은행업무

t = int(input())
# t = 1
for tc in range(1, t + 1):
    bin_num = list(map(int, list(input())))
    tri_num = list(map(int, list(input())))
    print(bin_num, tri_num)
    # bin_num = [1, 0, 1, 0]
    # tri_num = [2, 1, 2]
    bin_to_dec = tri_to_dec = 0
    # 2진수 10진수로 변환 int('0b' + input(), 2)
    for i in range(len(bin_num)):
        bin_to_dec += (bin_num[i] * (2 ** (len(bin_num) - 1 - i)))
    # 3진수 10진수로 변환
    for i in range(len(tri_num)):
        tri_to_dec += (tri_num[i] * (3 ** (len(tri_num) - 1 - i)))

    flag = 0
    for i in range(len(bin_num)):
        tmp = 2 ** (len(bin_num) - 1 - i)
        if bin_num[i]: # 1이면,
            # 0으로 바꿔줌, 빼기
            num1 = bin_to_dec - tmp
        else: # 0이면,
            # 1로 바꿔줌, 더하기
            num1 = bin_to_dec + tmp
        for j in range(len(tri_num)):
            tmp = 3 ** (len(tri_num) - 1 - j)
            if tri_num[j] == 2: # 2일 때
                num2 = tri_to_dec - tmp # 1로 바꿈
                if num1 == num2:
                    flag = 1
                    break
                num2 = num2 - tmp # 0으로 바꿈
                if num1 == num2:
                    flag = 1
                    break
            elif tri_num[j] == 1: # 1일 때
                num2 = tri_to_dec + tmp # 2로 바꿈
                if num1 == num2:
                    flag = 1
                    break
                num2 = tri_to_dec - tmp  # 0으로 바꿈
                if num1 == num2:
                    flag = 1
                    break
            else: # 0
                num2 = tri_to_dec + tmp  # 1로 바꿈
                if num1 == num2:
                    flag = 1
                    break
                num2 = num2 + tmp # 2로 바꿈
                if num1 == num2:
                    flag = 1
                    break
        if flag:
            break
    print('#{} {}'.format(tc, num1))