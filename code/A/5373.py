# 큐빙 5373.py

cube = [[['w'] * 3 for _ in range(3)], # 0: 윗면
        [['y'] * 3 for _ in range(3)], # 1: 아랫면
        [['r'] * 3 for _ in range(3)], # 2: 앞면
        [['o'] * 3 for _ in range(3)], # 3: 뒷면
        [['g'] * 3 for _ in range(3)], # 4: 왼쪽면
        [['b'] * 3 for _ in range(3)],] # 5: 오른쪽면\

t = int(input())
for _ in range(t):
    tc = int(input())
    act = list(input().split())
    a, b = 'L', '-'
    if a == 'L':
        if b == '-':
            
            cube[0][]
print(''.join(cube[0][0]))
print(''.join(cube[0][1]))
print(''.join(cube[0][2]))
