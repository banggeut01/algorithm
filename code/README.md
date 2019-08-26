# Day 1

Solving Club > list(7월 31일)

* 조망권 View
  * 소스보기 [소스보기](./1206.py)
  * best [소스보기](./1206풀이.py)



# Day 2

### SWEA

Lean > Course > IM > List1

* 1일차 - min max [소스보기](./4828.py)

* 1일차 - 전기버스 [소스보기](./4831.py)
  
  * 현재 위치가 N-K보다 작을 동안 반복 
  
  * 현재 위치 pos에서 갈 수 있는 만큼 최대한(pos+k) 간 후, 그 전에 위치한  가장 최근 정류장에서 충전
  
  * 운행할 수 없는 경우1:  현재 위치 pos에서 다음 충전기 정류장 pos+1까지 거리가 k보다 큰 경우
  
  * 운행할 수 없는 경우2: k*m이 n보다 작은경우
  
  * 정류장개수만큼 list. 충전기 있으면 1, 없으면 0. 정류장개수는 100이하. idx는 정류장위치.
  
  * error
  
    ```python
    for j in range(k, -1, -1): # => x
    for j in range(k, 0, -1): # k ~ 1까지
        
    # (n, m) => n ~ m-1
    # (m, n, -1) => m ~ n+1
    ```
  
* 1일차 - 숫자 카드 [소스보기](./4834.py)

  * 염겨레 방법

  ```python
  # 내코드
  ...      
  for i in range(1, 10):
      if cnt[i] >= max_cnt: # 더 개수가 크면
          max_cnt = cnt[i]
          max_num = i
  # 겨레코드 (좀 더 파이썬스러움)
  # list comprehension으로 0~9빈도수 리스트 채움
  ...
  # 최대값, 인덱스 구하는 코드
  max_cnt, max_num = (cnt[i], i) for i in range(1, 10) if cnt[i] >= max_cnt
  ```

* 1일차 - 구간합 [소스보기](./4835.py) 

  * 선생님 방법

  ```
  # 슬라이딩 윈도우
  A, B, C, D
  1회 합 : A+B+C
  2회 합 : B+C+D
  회차마다 더해주지 말고, 2회 때 1회합 - A + D
  시간복잡도 O(n)
  ```

Solving Club > list(8월 1일)

* Flatten, 평탄화 [소스보기](1208.py)

  * 인덱스 접근, 변수에 따로 저장해 접근 [소스보기](1208-2.py)

  ```python
  if box[i] > box[max_idx] # 비교할 때마다 인덱스로 접근하는 대신
  if box[i] > max_val # 변수에 저장하여 비교
  ```

  실행 결과 1.7~1.8 로 별 차이 없었음.

  * 내방법
  
  ```
  건물의 높이를 값으로 가지는 리스트.
  idx는 position
  최소값, 최대값 찾아 덤프 횟수만큼 평탄화
  ```
  
  * 염동환 방법
  
  ```
  높이 큰 것부터 빈도 세기 list 'up', idx = 개수(1 ~ 100)
  높이 작은 것부터 빈도 세기 
  덤프 수만큼 평탄화
  ```
  
  * 선생님 방법
  
  ```
  1. 빈도수 계산
  건물의 높이를 idx로 가지는 리스트. (0 ~ 100 값을 가짐)
  
  2. 최대 최소 찾기
  최소값은 idx = 0부터 처음으로 0이 아닌값을 갖는 idx
  최대값은 idx = 100부터 처음으로 0이 아닌 값을 찾는 idx
  
  3. 평탄화 작업
  최소값 빈도수 올리기, 최대값 빈도수 내리기
  ```
  
  

# Day 3

Solving Club > list(8월 7일)

* [2일차 - Sum 1209 소스보기](./code/1209.py)

  * input 값 100개씩 들어옴
  * 100 * 100 행렬
  * 1차원 리스트로 짜보기

  ```python
  # 1차원 리스트
  arr = []
  for _ in range(100):
      arr += list(map(int, input().split()))
      
  # 2차원 리스트
  arr = [list(map(int, input().split())) for _ in range(100)]
  ```

  * 1차원 리스트의 idx

  ```
  만약 2차원 배열 인덱스가 [67][8]이라면,
  1차원 배열 인덱스는 [67 * 100 + 8] 이다.
  ```
  
  * [1209풀이 - for문 한개 쓰기](./code/1209풀이.py)

[추가 문제 - 백준](https://www.acmicpc.net/problem/2578)

* [2578 빙고](./code/2578.py) 

  ```python
  # list copy 주의!
  row_cnt = col_cnt = [0]*5
  row_cnt[3] = 4
  print(row_cnt) # => [0, 0, 0, 4, 0]
  print(col_cnt) # => [0, 0, 0, 4, 0]
  ```

  ```python
  # error
  if i == j:
      check[10] += 1
  elif i + j == 4:
      check[11] += 1
  ```

  이렇게 하면, arr(i=2, j=2)=5 일 때, cross_cnt 한개만 카운트된다.

  따라서, elif가 아닌 if로 바꿔줘야 함.

  ```python
  if i == j:
      check[10] += 1
  if i + j == 4:
      check[11] += 1
  ```

  ```
  error
  주의!!
  반례 생각해주기
  계속 틀렸는데, 그 이유가 빙고 갯수를 3인 경우만 생각했기 때문!!
  2줄이 그어진 상태에서, 한 줄이 더 그어졌을 때
  빙고의 개수가 4가 될 수도 있다.
  ```

  

  ```python
  # 수정 전
  if bingo == 3:
      print(cnt)
      break
  ```

  ```python
  # 수정 후
  if bingo >= 3:
      print(cnt)
      break
  ```

  * 김준영 방법 (이렇게 풀어보기!)

  ```
  나의 방법) check = [0] * 12 # row_cnt:0~4, col_cnt:5~9, cross_cnt:10~11
  지워진 개수를 세어주는 리스트를 따로 만들었다.
  
  하지만, 이를 따로 만들지 않고 숫자를 지우는 방법도 있다.
  arr에서 숫자 0으로 변경 후 행순회, 열순회, 대각순회
  ```

추가문제 - SWEA

* [요리사 4012](./code/4012.py) (아직 안함)

  * 부분집합 문제
  * 부분집합 잘 모르니 일단 그냥 풀어보기

  ```
  식재료를 2그룹으로 나누어야 된다.
  N개의 식재료 --> N/2, N/2
  => 조합 문제(부분집합과 관련)
  원소의 개수가 N/2인 부분집합 찾으면 1그룹 나머지는 2그룹으로.
  N = 최대 16 --> 2^16 = 65,000
  
  가지치기하면 좀 더 빠르게 풀 수 있다!
  ```
  
  * 선생님 풀이
  
  ```python
  # 중복 상관없이 그냥 하기
  
  arr = 'ABCD'
  N = 4
  
  for set_num in range(1 << N):
      a, b = [], []
      for i in range(N):
          if set_num & (1 << i):
              a.append(arr[i])
          else:
              b.append(arr[i])
     if len(a) == len(b):
      	print(a, b)
          
  # ['A', 'B'] ['C', 'D']
  # ...
  # ['C', 'D'] ['A', 'B']
  ```
  
  
  
  

# Day 4

Lean > Course > IM > List2

* [색칠하기 4836](./4836.py)

```python
# 칠해지지 않은 상태에서 처음 칠할 때만 쓸 수 있음
# 두번째 칠할 때 부터는 어떤색인지 확인해야 함!
# 밑에 코드 쓰지 않기!
for i in range(r1, r2+1): # 위 -> 아래로 r1~r2
    gird[i][c1:c2+1] = [color] * (c2-c1) # c1~c2 개수만큼 color 변경
    
# for문 2개로 row, col 순회하며 color 확인
```

* [부분집합의 합 4837](./4837.py)
* [이진탐색 4839](./4839.py)

* [특별한 정렬 4843](./4843.py)

Solving Club > list(8월 8일)

* [7일차 - 금속막대 1259](./1259.py)

  * 수나사, 암나사 길이가 같은 나사는 존재하지 않음!
  * 연결되지 않는 나사 존재하지 않음!
  * 그냥 끼워넣기로 풀어보기

  ```
  1. 시작 나사를 찾기
     수나사와 대응되는 암나사가 없으면 시작 나사!
  2. 나사를 list에 삽입하면서 마지막나사인 암나사와 대응되는 수나사를 찾는다!
  3. 2를 n-2번(시작나사 제외) 반복한다 
  ```
  
  * 장은비 방법(재귀로 구현)
  
  ```
  def sort(screws, result, tmp):
  
  screws : 나사
  result : 답으로 출력할 리스트
  tmp
  
  screws에 있는 나사를 한 개씩 읽음.
  연결이 되면 result
  연결이 안되면 tmp
  tmp + result
  
  return sort(tmp, result, [])
  ```
  
  * 선생님 방법
  
  ```
  순열 만드는 방법, 모든 방법 단순한 방법
  하나씩 연결하면서 안되면 가지치기
  순열 생성 아직 재귀로 하는 것 안 배움! 나중에 배우면 해보기!
  ```
  
  * SWEA 화학물질2 비슷한 문제 풀어보기! 순열, DP

추가 문제 - 백준

 * [색종이 10163](./10163.py)
   
    * [사이트](https://www.acmicpc.net/problem/10163)
    
 * [숫자카드 10815](./10815.py) 
   
   * [사이트](https://www.acmicpc.net/problem/10815)
   * 첫번째시도) 초기 완전탐색 코드 시간초과!
   * 두번째시도) 이진 탐색
     * 상근이 카드 정렬 시킨 후 할 것
     * 이 때, sorted() 써도 되는지.. 모르겠지만 일단 써보자.
   
   ```python
   # error
   if your > my[mid]:
     left = mid
   elif your < my[mid]:
     right = mid
   ```
   
   ```
   위와 같이 하게 되면,
   반복문 빠져나올 수 없다.
   이미 검사한 mid 위치를 제외하고 검사해야한다.
   아래와 같이 바꿈.
   ```
   
   ```python
   if your > my[mid]:
     left = mid + 1
   elif your < my[mid]:
     right = mid - 1
   ```
   
   ```
   또한, while 조건문도 다음과 같이 바꾸어줌
   ```
   
   ```python
   while left != right: # 수정 전
   while left <= right: # 수정 후
   ```
   
   
   
   * 김태우 방법(set 이용)
   
   ```
   상근 카드 set
   검사할 카드 list
   
   set은 이진탐색트리, 해싱으로 구현되어 있음
   map, set, hashmap, hashset 등..
   
   주의) set은 순서를 보장하지 않음! indexing x
   ```
   

# Day 5

SWEA

* [String 1221.py](./1221.py)
  * 내 방법은 dictionary에 개수 세어 저장하고 출력하는 방식.
  * 굳이 이렇게 할 이유가 없음
  * 세면서 바로 출력하게 하기!
* [간단한 압축 풀기 1946.py](./1946.py)

# Day 6

SWEA > Learn > Course > IM > 파이썬 - String

* [문자열 비교 4864.py](./4864.py)
  
  * 브루트 포스로 풀어보자.
  * 다른 방법으로도 풀어보기!
  
* [회문 4861.py](./4861.py) 

  * 추윤형 코드 [4861chu.py](./4861chu.py)

  ```
  이중 for문 나오기 위해 flag 라는 변수를 이용!
  ```

  * 정지수 코드

  ```
  한 함수로 가로, 세로 검사 모두 가능하도록 함!
  지금 나의 방법은 가로, 세로 검사 따로 함수를 만들었음
  행,열 바꾸기를 이용함
  
  데이터가 크지 않을 경우,
  이 방법이 더 좋다고 함!
  ```

  

* [글자수 4865.py](./4865.py)

추가문제 - SWEA

* [세상의 모든 팰린드롬 2 4579.py](./4579.py)
* [세상의 모든 팰린드롬 4522.py](./4522.py)
* [자기 방으로 돌아가기 4408.py](./4408.py)

[추가문제 - 백준](https://www.acmicpc.net/problem/1244)

* [스위치 켜고 끄기 b1244.py](./b1244.py) 

  ```python
  # error 출력형식이 잘못되었습니다.
  # 아래 두 코드 시도해봐도 안됨
  # 1)
  print(' '.join(map(str, switch)))
  
  # 2)
  for i in range(sw_len - 1):
      print(switch[i], end=" ")
  
  print(switch[i + 1])
  ```

  문제 출력 조건 제대로 읽기! (**한 줄에 20개씩 출력**)

  아래와 같이 바꾸었다.

  그런데, ...

  ```python
  # runtime error!
  switch = list(map(str, switch))
  while len(switch) >= 20:
      print(' '.join(switch[20]))
      tmp -= 20
      switch = switch[20:]
  print(' '.join(switch))
  ```

  왜 그런지는 모르겠으나 아래와 같이 수정 후 pass

  ```python
  s = 0
  tmp = sw_len
  switch = list(map(str, switch))
  while tmp >= 20:
      print(' '.join(switch[s:s+20]))
      tmp -= 20
      s += 20
  print(' '.join(switch[s:]))
  ```

  아마 `switch = switch[20:]` 이 부분이 원인인듯 하다.

  앞으로 이러한 코드는 쓰지 않는 걸로..

Solving club > 03.String(8월 16일)

* [회문1 1215.py](./1215.py) 

  ```
  index 주의하기!
  가장 많이 뜬 에러 out of range index
  
  윤형씨 팁)
  인덱스 에러가 뜰 때 마지막 범위 + 1 해보고 돌려보기
  
  검사 범위 (text길이8, 회문길이4 일 때)
  행 검사: row는 0 ~ 7 / col은 0 ~ 4
  열 검사: col은 0 ~ 7 / row는 0 ~ 4
  ```

  ```
  start = (0 ~ N -M)
  end = start + m - 1
  비교 횟수 m // 2
  ```
  
  * 선생님 풀이
  
    * 슬라이싱 쓰면 속도가 느려지고, 메모리 많이 쓴다!
  
    * 나의 코드 경우에 p라는 현재 위치 변수 만들었지만, 
  
      선생님 경우 start, end위치 저장하는 변수 따로 만들었음
  
  ```python
  for tc in range(1, 11):
      m = int(input()) # 회문 길이
      word = [input() for _ in range(8)]
      
      ans = 0
      
      idx = 0
      # 한 행/열(idx:0)에 대해서,
      for s in range(8 - m + 1):
      	e = s + m - 1 # end, start
          for i in range(m // 2): # 행우선순회
              if arr[idx][s + i] != arr[idx][e - i]: break
          else:
              ans += 1
          for i in range(m // 2): # 열우선순회
              if arr[s + i][idx] != arr[e - i][idx]: break
          else:
              ans += 1
  ```
  
* [회문2 1216.py](./1216.py) 

  * 선생님 코드 

  ```python
  for tc in range(1, 11):
      m = int(input()) # 회문 길이
      word = [input() for _ in range(8)]
      
      ans = 1 # 지금까지 찾은 최대 길이
      # 한 행/열에 대해서,
      for idx in range(100):
          for s in range(100): # 시작 위치
              for e in range(99, s, -1): # 끝 위치, 99 ~ 0
                  L = e - s + 1 # L 현재 길이
                  if L <= ans: break
          		for i in range(L // 2): # 행우선순회
              		if arr[idx][s + i] != arr[idx][e - i]: break
         			else:
              		ans = L
                  if L <= ans: break
          		for i in range(L // 2): # 열우선순회
              		if arr[s + i][idx] != arr[e - i][idx]: break
          		else:
              		ans = L
  ```

  * 다른 방법 (한번 구현해보기)
    * 인접한 부분 비교, 같을 때까지
    * 회문 길이가 짝수, 홀수인 경우로 나눠 비교해야함
    * 기준 위치를 잡아야함 (홀수의 경우 가운데/짝수 경우 왼쪽 or 오른쪽)

  ```python
  for tc in range(1, 11):
      m = int(input()) # 회문 길이
      word = [input() for _ in range(8)]
      
      ans = 1 # 지금까지 찾은 최대 길이
      # 한 행/열에 대해서,
      for idx in range(100):
          for x in range(100): # x => 기준 위치
              # 회문 길이가 짝수
              # 행에 대해서
              l, r, cnt = x, x + 1, 0 # cnt는 회문 길이
              while l >= 0 and r < 100:
                  if arr[idx][l] != arr[idx][r]: break
                  l, r, cnt = l - 1, r + 1, cnt + 2
              ans = max(ans, cnt)
              # 열에 대해서 
              l, r, cnt = x, x + 1, 0
              while l >= 0 and r < 100:
                  if arr[l][idx] != arr[r][idx]: break
                  l, r, cnt = l - 1, r + 1, cnt + 2
              ans = max(ans, cnt)
              
              # 회문 길이가 홀수
              # 행에 대해서
              l, r, cnt = x - 1, x + 1, 1
              while l >= 0 and r < 100:
                  if arr[idx][l] != arr[idx][r]: break
                  l, r, cnt = l - 1, r + 1, cnt + 2
              ans = max(ans, cnt)
              # 열에 대해서 
              l, r, cnt = x - 1, x + 1, 1
              while l >= 0 and r < 100:
                  if arr[l][idx] != arr[r][idx]: break
                  l, r, cnt = l - 1, r + 1, cnt + 2
              ans = max(ans, cnt)
  ```

# Day 7

SWEA > IM > stack1

* [4일차 괄호검사 4866.py](./4866.py)

* [Ladder 1](./1210.py)

  * 김준영 방법 : 거꾸로 생각하기

  ```python
  맨 위부터 찾지 않고,
  마지막 행부터 찾는다.
  2를 먼저 찾아서 위로 올라가는 방식!
  헿
  ```

  * [재귀로 해보기](./1210-2.py)

  ```
  김준영 방법으로 첫번째 행부터 말고, 마지막 행부터!
  결과를 찾아 올라가기!
  ```
  
  * [선생님 풀이1 - 반복문 (내 방법과 같음)](./1210solution.py)

    * 조건에 따른 좌표 이동과 방향 설정
  
      1. 오른쪽 길 있으면 이동, 방향 설정
      2. 왼쪽 길 있으면 이동, 방향 설정
      3. 위로 이동
      4. 왼쪽에 길이 있으면 이동
      5. 위로 이동, 방향 설정
      6. 오른쪽에 길 있으면 이동
      7. 위로 이동, 방향설정
  
    * 위 경우는 3가지로 묶을 수 있음 (1,2,3), (4, 5), (6, 7)
  
    * 방향 상태 저장하는 변수 direction = 위 or 왼쪽 or 오른쪽
    
    ```python
    dir = 0 # direction 0: 위, 1: 왼쪽, 2: 오른쪽
    while x:
        if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
            y, dir = y - 1, 1
        elif dir != 1 and y + 1 < 100 and arr[x][y + 1]:
            y, dir = y + 1, 2
        else:
            x, dir = x - 1, 0
    ```
    
    ```python
        while x:
        if y - 1 >= 0 and arr[x][y - 1]:
            while y - 1 >= 0 and arr[x][y - 1]:
                y -= 1
        elif y + 1 < 100 and arr[x][y + 1]:
            while y + 1 < 0 and arr[x][y - 1]:
                y += 1
        x -= 1
    ```
    
  * [선생님 풀이 2(재귀)](./1210solution.py)
  
    * 나의 재귀와 다르게 visit라는 방문 리스트를 따로 만들지 않고,
  
      가지고 있는 경로 변수를 이용함
  
    ```python
        def DFS(x, y):
        if x == 0: return y
        
        arr[x][y] = 0 # 이 부분 주목!
        if y - 1 >= 0 and arr[x][y - 1]:
            return arr(x, y - 1)
        elif y + 1 < 100 and arr[x][y + 1]:
            return arr(x, y + 1)
        else:
            return arr(x + 1, y)
    ```
  
    
  


# Day 8

SWEA > IM > stack1

* 4869.4일차 - 종이붙이기

  * 점화식 문제 - 보통 n에 대한 문제 풀 때는, n-1은 다 완료되어있다 생각하기
  * 더 작은 문제로 큰 문제를 해결하자

  ```
  f(1), f(2)
  n=1일 때 1가지
  n=2일 때 3가지(가로2개, 세로2개, 큰거1개)
  
  f(0)이면, 안만드는법 1가지!
  
  길이 n일 때,
  n-1에 10짜리 붙이는 방법 1가지!
  n-2에 1)20짜리 가로직사각형2개로, 2)20짜리 큰 사각형 1개로 2가지!
  (세로2개는 n-1에 10짜리 붙이는 방법에 포함!)
  ```

  * [재귀](./4869.py)
  * [DP](./4869-2.py) 

* 4871 [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

  * [스택 사용](./4871-2.py) 해결하지 못하였음!

    ```python
    # runtime error!
    def DFS(v, g):
        stack = []
    
        visit[v] = True
        stack.append(v)
    
        while s: # 빈 스택 아닐동안
            for w in matrix[v]:
                if not visit[w]: # 가지 않았던 노드
                    if w == g:
                        return 1
                    visit[w] = True # 방문
                    stack.append(w)
                    v = w
                    break
            else: # 갈 수 있는 노드 없으면, 
                stack.pop()
                if stack:
                    v = stack[-1] # 되돌아가기
        return 0
    ```

    * 이유를 모르겠다. 원래 재귀로 푸는 것인가..???
    * 해결하지 못하였음!

  * [재귀 사용](./4871.py)

    * ??? 의문점) 재귀로 쓰는 DFS는 중간에 stop하지 못하는가..?

    ```python
    # error1
    def DFS(v, g): # v 현재 노드, g 도착 노드
        if v == g:
            return 1
        
        visit[v] = True
    
        for w in matrix[v]:
            if not visit[w]:
                route.append(w)
                return DFS(w, g)
       	return 0
    ```

    ```결과
    #1 1
    #2 1
    #3 None
    ```

    ```python
    # error2
    def DFS(v, g): # v 현재 노드, g 도착 노드
        if v == g:
            return 1
        
        visit[v] = True
    
        for w in matrix[v]:
            if not visit[w]:
                route.append(w)
                DFS(w, g)
    ```

    ```
    #1 None
    #2 None
    #3 None
    ```

    ```python
    # error3
    def DFS(v, g):  # v 현재 노드, g 도착 노드
        if v == g:
            return 1
    
        visit[v] = True
    
        for w in matrix[v]:
            if not visit[w]:
                route.append(w)
                DFS(w, g)
        return 0
    ```

    ```
    #1 0
    #2 0
    #3 0
    ```

    ```python
    # 해결
    def DFS(v):
        visit[v] = True
    
        for w in matrix[v]:
            if not visit[w]:
                route.append(w)
                DFS(w)
                
    ...
    route = []
    
    DFS(s)
    for r in route:
        if r == g:
            result = 1
            break
        else:
            result = 0
    ```

    DFS 중간에 중단하지 않고, 모두 수행한 후

    route 중 도착지점 있는지 검사하였다.

  * 정지수 해결법 ==> flag 변수 사용

    ```python
    ## 그래프 경로 4871.py
    # 유향 그래프
    # 재귀 DFS
    def DFS(v):
       flag = 0
       visit[v] = True
       if v ==g:
           return 1
       for w in matrix[v]:
           if not visit[w]:
               flag = DFS(w)
               if flag == 1:
                   break
       return flag
    t = int(input())
    for tc in range(1, t + 1):
       v, e = map(int, input().split()) # 노드, 엣지
       matrix = [[] for _ in range(v + 1)]
       # 인접행렬
       for _ in range(e):
           start, end = map(int, input().split())
           matrix[start].append(end)
       s, g = map(int, input().split()) # 시작, 도착노드
       visit = [False] * (v + 1) # 방문 노드
       print('#{} {}'.format(tc, DFS(s)))
    ```

    

* [4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 D](./4873.py)

추가문제

SWEA > Soving Club

* 작업순서 1267

  * DFS-스택, [DFS-재귀](./code/1267-2.py), [DAG-queue](./code/1267-3.py) 세가지 방법으로 풀어보았다.
  * DFS-스택, 재귀는 답을 스택에 저장해 거꾸로 출력
    * 방문하면서 위상순서 리스트에 저장하는 것이 아닌
    * 더 이상 갈 노드가 없을 때, 위상순서에 저장하였고
    * 이를 거꾸로 출력한 것이 답이다.
  * DAG-큐는 위상순서 그대로 출력
    * visit 대신 indegree 리스트를 사용하였음
  * [dfs스택 - 소스보기](./1267.py) 

  ```python
  # 항상 스택 접근할 때 isEmpty 주의한다!
  if tmp_stack: 
      v = tmp_stack[-1] # 되돌아가기
  ```

  * DFS로 푸는데 문제점 발생!  (DAG로도 풀어보기!)

  ```
  시작노드 찾기)
  
  들어오는 indegree 0이면서, outdegree 1이상
  
  => 결과 Fail
  
  왜?
  시작 노드가 한개만 존재하는 것이 아니다.
  아래 그림을 예로, a, g 모두 시작노드가 된다.
  
  그렇다면 시작노드에서 시작한 후, 터미널 노드까지 갔을 때
  다시 돌아오면서 방문하지 않은 노드를 찾아야한다.
  예)
  a -> b -> c 까지 온 후,
  c에서 outdegree 0이므로 이 때 1) stack에 넣어줌!
  stack을 2개 써야함
  
  1) 방문 순서 저장할 stack
  2) 돌아갈 노드 저장할 stack
  
  자세한 방법은 위상정렬 - 2)DFS 보기!
  ```

  * error
    * v(노드)와 result_stack의 길이는 같아야 하지만, v값이 더 크다.
      방문하지 않은 노드가 존재한다!
      어디서 놓쳤을까?

  ```python
  # 10 tc 중 6개만 맞음
  # 왜?
      print(v)
      print(len(result_stack))
  ```

  * 문제 코드

    ```python
    for s in range(1, v + 1):
        if outgoing[s] and indegree[s] == 0: # 시작노드이면,
            dfs(s)# DFS 시작
    ```

  * 해결 코드

    ```python
    for s in range(1, v + 1):
        if indegree[s] == 0:: # 시작노드이면,
            dfs(s)# DFS 시작
    ```

    * 왜?
      * 혼자 떨어져 있는 노드가 존재함
      * [input data](./day9/1210input.txt)의 in, out node에는 존재하지 않음
      * 예로 test case 6번의 {160, 137, 172, 140, 119}번 노드들
      * 모두 다 연결된 상태는 아님

  * 위상 정렬 - 1) DAG(Directed Acyclic Graph) (indegree, outdegree고려)

    ![dag](./images/dag.png)

    *  **들어오는 엣지를 Incomming** **/나가는 엣지를 Outgoing**
    * **엣지의 개수를 Indegree** /**나가는 엣지의 개수를 Outdegree**
    * BFS와 비슷한 방법이다.
    * 작업의 우선순위를 표현할 때 DAG 구조를 가짐
    * Queue 이용해야한다.
    * 진입 차수 계산(정점번호 idx로, 모든 정점의 진입차수 계산)
      * v에서 나가는 간선의 개수
    * 들어오는 화살표 없는(진입차수가 0인) 정점 Queue에 넣기
      * FIFO
    * v의 인접정점(u) 찾아 진입차수 1감소
      * u의 진입차수 0이 되면 u를 큐에 삽입

    ![dag](./images/dag.png)

    ```python
    arr = [0, 1, 2, 2, 2, 1, 0]
    	 # a, b, c, d, e, f, g 
    
    
    queue = [a, g] # indegree 0 큐에 삽입
    arr = [0, 0, 2, 1, 2, 1, 0] # queue[0]인 a의 인접정점 indegree -1
    result = [a] # 위상순서 a
    queue = [g, b] # 인접정점 indegree 0 이 되면, queue에 삽입
    
    arr = [0, 0, 2, 0, 2, 1, 0] # g의 인접정점 indegree -1
    result = [a, g]
    queue = [b, d]
    
    arr = [0, 0, 1, 0, 1, 1, 0]
    result = [a, g, b]
    queue = [d]
    
    arr = [0, 0, 1, 0, 0, 1, 0] # d의 인접정점 e의 indegree -1
    result = [a, g, b, d]
    queue = [e]
    
    arr = [0, 0, 0, 0, 0, 0, 0] # d의 인접정점 e의 indegree -1
    result = [a, g, b, d, e]
    queue = [c, f]
    
    result = [a, g, b, d, e, c, f]
    queue = []
    ```

    ```python
    # python에서 큐 구현은 아래와 같이 import하여 사용함
    from collections import deque
    
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.append(4) # => [1, 2, 3, 4]
    dq.popleft() # => [2, 3, 4]
    ```

    

  * 위상 정렬 - 2) DFS (outdegree만 고려)

    * 위의 예제로 보자
      * **시작점이 주어질 땐, 방문할 때마다 result_list에 넣었다.**
      * **방문 끝나면 들어온 순서대로 출력**
      * 이 예제는 시작점이 주어지지 않음!
      * 따라서 **더 이상 갈 노드가 없을 때 result_stack에 넣는다.**
      * **방문 끝나면 거꾸로 출력!**

    ```
    a에서 시작! (outgoing이 존재함)
    stack = [a]
    stack = [a, b]
    stack = [a, b, c] => 갈 노드가 없음! result_stack = [c]
    stack = [a, b]
    stack = [a, b, e]
    stack = [a, b, e, f] => 갈 노드가 없음! result_stack = [c, f]
    stack = [a, b, e] => 갈 노드가 없음! result_stack = [c, f, e]
    stack = [a, b] => 갈 노드가 없음! result_stack = [c, f, e, b]
    stack = [a]
    stack = [a, d] => 갈 노드가 없음! result_stack = [c, f, e, d]
    stack = [a] => 갈 노드가 없음! result_stack = [c, f, e, d, a]
    stack = []
    
    g에서 시작! (indegree 0, outdegree 1이상)
    stack = [g] => 갈 노드가 없음! result_stack = [c, f, e, d, a, g]
    ```

    * indegree 0인 곳에서 시작!
    * 더 이상 진입할 노드 없을 때, 다시 돌아감
      * 현재 노드를 스택에 저장
    * 거꾸로 출력! (stack pop)

* [쇠막대기 자르기 5432](./5432.py) 아직 푸는 중!

# Day 9

오늘은 백트래킹에 대해서 배웠다.

Lean > Course > IM > List2 [부분집합의 합 4837](./4837.py) 문제를

백트래킹 이용해 다시 풀어보겠다.

* [부분집합의 합 4837-2](./4837-2.py)

  * 가지치기 해보기

  ```python
  # error!
  def subset(k, n, tmpsum):
      global result
      if tmpsum > setsum:
          return
      if k == n:
          if tmpsum == setsum: # => 1)이부분 잘못됨!
              result += 1
          return
      subset(k + 1, n, tmpsum + uset[k]) # 왼쪽
      subset(k + 1, n, tmpsum) # 오른쪽
      
  uset = [i for i in range(1, 13)]
  t = int(input())
  for tc in range(1, t+1):
      n, setsum = map(int, input().split())
  
      result = 0
      subset(0, n, 0) # => 2)이부분 잘못됨!
  
  
      print('#{} {}'.format(tc, result))
  ```

  1)부분집합원소의 수를 체크하지 않았다! 

  2)12 높이까지 모두 확인해야함 (여기서 높이는 루트노드에서 현재노드까지 경로를 의미함)

  `subset(0, 3, 0)` 이면 높이 3까지만 확인함

  문제에서는 부분집합원소개수, 부분집합원소합 두가지 조건 충족해야한다고 하였음

  아래와 같이 바꿈!

  ```python
  # 해결!
  def subset(k, n, cnt, tmpsum): # cnt = 현재 선택한 원소수, tmp_sum: 원소들 합
      global result, ele_cnt, setsum
      if tmpsum > setsum:
          return
      if k == n:
          if tmpsum == setsum and cnt == ele_cnt:
              result += 1
          return
      subset(k + 1, n, cnt + 1, tmpsum + uset[k]) # 왼쪽(1:포함)
      subset(k + 1, n, cnt, tmpsum) # 오른쪽(0:미포함)
  
  uset = [i for i in range(1, 13)]
  t = int(input())
  for tc in range(1, t+1):
      ele_cnt, setsum = map(int, input().split())
  
      result = 0
      subset(0, 12, 0, 0)
  
  
      print('#{} {}'.format(tc, result))
  ```
  
* **여기서 중요한 점!** 
  
  * 지역변수를 영역 밖에서 사용할 때, `global`로 선언하고 써야함
  
  * 단순히 값이 몇인지 확인할 수 있지만,
  
  * 변수의 값을 바꿀 순 없다.
  
  * 하지만 리스트는 그냥 썼는데?
  
    * 김준영 피셜) 리스트는 객체이기 때문에 인자로 넘기지 않고도 변경이 가능했던 것!
  
      ```python
      # 변경할 수 없음
      
      def test():
          print(a)
          a = a + 1
          
      a = 3
      test()
      
      # error!
      # UnboundLocalError: local variable 'a' referenced before assignment
      ```
  
      ```python
      # 값이 몇인지는 알 수 있음
      
      def test2():
          print(a)   
          
      a = 3
      test2() # => 3
      ```
  
      ```python
      # global 선언
      
      def test3():
          global a
          a += 1
          print(a)
          
      a = 3
      test3()
      4
      ```
  
      

SWEA > Soving Club

* [1220 Magnetic](./code/day9/1220.py) 미완성코드!