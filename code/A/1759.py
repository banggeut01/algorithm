# 1759 암호만들기
import copy
def backtrack(k, start, vcnt, ccnt, tmp): # k:선택된 암호 개수, start:선택시작위치, vcnt:모개수, ccnt:자개수
    pwd = copy.deepcopy(tmp)
    
    if k == L:
        if vcnt >= 1 and ccnt >= 2:
            print(''.join(pwd))
        return

    for i in range(start, C): 
        pwd.append(alpha[i])
        if alpha[i] in vowel: # 모음이면,
            backtrack(k + 1, i + 1, vcnt + 1, ccnt, pwd)
        else:
            backtrack(k + 1, i + 1, vcnt, ccnt + 1, pwd)
        pwd.pop()

L, C = map(int, input().split()) # L:암호길이, C:알파벳개수
alpha = sorted(list(input().split()))
vowel = list('aeiou')
backtrack(0, 0, 0, 0, []) 