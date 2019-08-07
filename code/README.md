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

[추가 문제](https://www.acmicpc.net/problem/2578)

* [2578 빙고](./code/2578.py)







