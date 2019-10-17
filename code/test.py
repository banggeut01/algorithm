    time, ch = stop.pop(0)
    time = int(time)
    while True:
        second += 1
        '''
        뱀 이동
        '''
        if second == time:
            # 직진 다하고, 방향을 틀어줘야함
            if ch == 'L': # 왼쪽
                dir = left[dir]
            else: # 오른쪽
                dir = right[dir]
            if stop:
                time, ch = stop.pop(0)
                time = int(time)
