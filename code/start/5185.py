# 5185.py 이진수
t = int(input())
for tc in range(1, t + 1):
    N, hex_num = input().split()
    N = int(N)
    result = []
    for i in range(N):
        bin_num = bin(int('0x' + hex_num[i], 16)) # 4(16) => 0b100
        bin_num = bin_num[2:] # 100
        for _ in range(4 - len(bin_num)):
            result.append('0') # ['0']
        for x in bin_num:
            result.append(x) # ['0', '1', '0', '0']
    print('#{} {}'.format(tc, ''.join(result)))