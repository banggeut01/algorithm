# 글자수 4865.py

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()

    # str1 중복 제거
    word = set()
    for char in str1:
        word.add(char)

    max_cnt = 0
    for w in word:
        cnt = 0
        for s in str2:
            if w == s:
               cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))