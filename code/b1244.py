# b1244.py

sw_len = int(input())
switch = list(map(int, input().split()))
stu_len = int(input()) # 학생수
for _ in range(stu_len):
    # gen 성별 1:남, 2:여
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(sw_len):
            if not (i + 1) % number:
                switch[i] = int(not bool(switch[i]))
    else:
        scope = min(sw_len - number + 1, number)
        number -= 1
        for i in range(scope):
            if switch[number + i] == switch[number - i]:
                switch[number + i] = switch[number - i] = int(not bool(switch[number - i]))
            else:
                break
s = 0
tmp = sw_len
switch = list(map(str, switch))
while tmp >= 20:
    print(' '.join(switch[s:s+20]))
    tmp -= 20
    s += 20
print(' '.join(switch[s:]))