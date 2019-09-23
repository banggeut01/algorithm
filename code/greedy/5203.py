# 5203.py 베이비진 게임

def is_babygin(i, c):
    if c[i] == 3: # run
        return True
    # triplet
    if -1 < i - 1 and c[i - 1]:
        if -1 < i - 2 and c[i - 2]:
            return True # i-2,i-1,i
        elif i + 1 < 10 and c[i + 1]:
            return True # i-1,i,i+1
    if i < 8 and c[i + 1] and c[i + 2]:
        return True # i,i+1,i+2

    return False

t = int(input())
for tc in range(1, t + 1):
    card = list(map(int, input().split()))
    c1, c2 = [0] * 10, [0] * 10

    for i in range(6):
        c1[card[i * 2]] += 1
        if is_babygin(card[i * 2], c1):
            print('#{} 1'.format(tc))
            break
        c2[card[i * 2 + 1]] += 1
        if is_babygin(card[i * 2 + 1], c2):
            print('#{} 2'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))