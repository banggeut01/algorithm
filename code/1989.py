# 펠린드롬, 회문 1989.py

n = int(input())

for tc in range(1, n+1):
    word = input()
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n - 1 - i]:
            print('#{} 0'.format(tc))
            break;
    else:
        print('#{} 1'.format(tc))