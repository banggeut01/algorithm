# GNS 1221.py

T = int(input())
en_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(T):
    tc, n = input().split()
    num_list = list(input().split())

    n = int(n)

    num_dict = {}
    for num in num_list:
        if num_dict.get(num): # 이미 있는 값이면
            num_dict[num] += 1 # 개수 증가
        else:
            num_dict[num] = 1

    print(tc)

    for en in en_num:
        if num_dict.get(en): # 개수 0아니면
            for _ in range(num_dict[en]): # 개수만큼
                print(en, end=" ") # 영어 숫자 출력

    print()

