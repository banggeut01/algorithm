# b1244.py

sw_len = int(input())
switch = list(map(int, input().split()))
stu_len = int(input()) # 학생수
print(switch)
for _ in range(stu_len):
    # gen 성별 1:남, 2:여
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(sw_len):
            if not (i + 1) % number:
                print(i)
                switch[i] = int(not bool(switch[i]))
    else:
        scope = min(sw_len - number, number - 1)
        for i in range(scope):
            if switch[number - 1 + i] == switch[number - 1 - i]:
                switch[number - 1 + i] = switch[number - 1 - i] = int(not bool(switch[number - 1 - i]))
            else:
                break
    print(switch)
print(' '.join(map(str, switch)))

