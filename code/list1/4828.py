# min max
import sys
sys.stdin = open('4828input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    min_num = max_num = numbers[0]
    for number in numbers[1:]:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
    result = max_num - min_num
    print('#{} {}'.format(tc+1, result))

