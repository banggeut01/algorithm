# APS 기본

* APS(Algorithm Problem Solving)

* (수) 실습 1문제, (목) 실습 5개(4개 + 1개)

  * Gitlab에 repository 생성
  * 교수님 초대
  * 소스코드명에 문제번호 포함

* 표준 스트림(standard streams)

  * 표준 입력(stdin) - keyboard
  * 표준 출력(stdout) - console
  * 표준 오류(stderr)

  ```python
  import sys
  sys.stdin = open('input.txt', 'r')
  # input.txt 파일을 표준 입력으로 간주하여 받겠다.
  ```

  

* python이 다른 컴파일 언어와 다른점?
  * c, java 변수 선언... , 컴파일러 이용.
  * python 인터프리터. 
  
* 초반 알고리즘 연습시 최대한 내장 함수, 라이브러리 쓰지 않고 구현하기!
  * len(), append(), 리스트 컴프리헨션 외에 다른 것 쓰지 않기
  * list slicing 쓰지 않기

## 1. 배열(List) 1 

### 알고리즘 시간복잡도
* 알고리즘 : 컴퓨터가 일을 하는 과정 기술한 것. 문제 해결 위한 절차.

* 알고리즘 표현 방법
  * 슈더코드 : 텍스트
  * 순서도 : 그림
  
* APS 과정의 목표 : 좋은 알고리즘 이해, 활용

* 좋은 알고리즘?
  * 정확성
  * **작업량** : 얼마나 적은 연산, 얼마나 CPU 적게 쓰나, 실행시간과 관련.
  * **메모리 사용량**
  * 단순성
  * 최적성 : 더 이상 개선 여지 없이 최적화되었는가.
  
* 알고리즘 성능
  * 성능 분석 기준으로 대부분 알고리즘의 **작업량**을 비교함.
  
  * 작업량은 **시간복잡도**로 표현함.
  
  * 시간 복잡도
  
  * 실제 걸리는 시간 -> 측정 힘듬
    
    * **실행되는 명령문 개수(연산 횟수) 계산**
    
      ``` python
      def func(n):
          # 명령문 - 1번
          for i in range(n):
              # 명령문 - n 번
              for j in range(i, n):
                  #명령문 - n * (n + 1)/2
      ```
    
  * 시간 복잡도 - 빅-오(O) 표기법 => 최악의 경우
  
    * 시간 복잡도 함수 중 가장 큰 영향력 주는 n에 대한 항만을 표시
    * 계수(Coefficient) 생략
    * O(1) 은 어떤 데이터든 시간 복잡도 같음.
  
  * 오메가(Ω) 표기법 => 최선의 경우
  
  * 쎄타(θ) 표기법 => 최악 == 최선
  
  * 예시
  
    ```html
    배열에 n개의 정수값이 있을 때, key를 찾는 문제
    ```
  
    * 순차검색 : idx 0부터 n-1까지 key값과 비교하는 방법. 최선 : 1번, 최악 : n번.
    * 이진탐색 : 정렬된 배열에서 검색. 1/2 중간위치부터 비교. 최선 : 1번, 최악 : log2n번.
  
  * ![빅오시간복잡도](./image/빅오시간복잡도.png)
  
    * 다항식 O(1) ~ O(n^2) 비교적 쉬운 문제
    * O(2^n), O(n!) NP
  
* 정렬 알고리즘 시간복잡도
  
  ![정렬알고리즘시간복잡도](./image/정렬알고리즘시간복잡도.png)
  
### 버블 정렬

  * 인접한 두 개 자료 비교해 자리 교환하는 방식
  
  * 한 단계가 끝나면 가장 큰 자료 마지막 자리로 정렬됨.
  
  * 예시)
  
    ```python
      # 내부 for문부터 이해하기
      arr = [55, 7, 78, 12, 42]
      
      n = len(arr)
      for i in range(n-1): # n -1 ~ 1
          if arr[i] > arr[i+1]:
              arr[i], arr[i+1] = arr[i+1], arr[i]
      		# => [7, 55, 12, 42, 78]   
              
      for i in range(n-2):
          if arr[i] > arr[i+1]:
              arr[i], arr[i+1] = arr[i+1], arr[i]
              # => [7, 12, 42, 55, 78]
             
      for i in range(n-3):
          ...
          
      for i in range(1): # i == 0    
    ```
  
    ```python
      # 버블 정렬 완성
      arr = [55, 7, 78, 12, 42]
      
      n = len(arr)
      for j in range(n-1, 0, -1):
          for i in range(j):
              if arr[i] > arr[i+1]:
              	arr[i], arr[i+1] = arr[i+1], arr[i]
    ```

### 카운팅 정렬 

  * O(n + k), n: 리스트 길이, k: 최대값
    
  * 자료값의 빈도수 계산해서 정렬하는 방법
    
  * 제한 사항
    
    * 저장되는 자료 양의 정수여야 함. (자료값을 리스트의 인덱스로 사용할 것이기 때문.)
    * 가장 큰 값을 알아야 함. (리스트 범위 지정 위해.)
    
  * 예시)
    
    ```python
      arr = [0, 4, 1, 3, 1, 2, 4, 1]
      # 양의 정수, 최대값을 알아야 된다.
      # 최대값 = 4
      cnt = [0] * 5 # 배열의 인덱스 n-1 = 4
      
      # 빈도수 계산
    for val in arr:
          cnt[val] += 1
      # cnt => [1, 3, 1, 1, 2]
      
      # 누적 빈도수 계산 => 옮겨질 위치
      for i in range(1, len(cnt)):
          cnt[i] = cnt [i-1] + cnt[i]
      
      # cnt => [1, 4, 5, 6, 8]
      # 옮겨질 위치 뒤에서부터 채움
      # arr 끝부터 읽으면서 cnt 1씩 깎고 위치에 넣음
      # 1은 4번째, 4는 8번째...
      
      #...(생략, 채워보기)
      
    ```
    
    ```python
      arr = [0, 4, 1, 3, 1, 2, 4, 1]
      cnt = [0] * 5
      
      for val in arr:
          cnt[val] += 1
      
      sorted_list = []
      for i in range(len(cnt)):
          for j in range(cnt[i]):
              # i가 cnt[i] 만큼 반복되는 것
              sorted_list.append(i)
      print(sorted_list)
    ```

### 배열 활용 예제 : Gravity

* 각 열의 인덱스 0, 1, ,,, , 8 
* 상자 개수 저장. [7, 4, 2, 0, 0, 6, 0, 7, 0]
* A상자 낙차 : (A상자 인덱스 ~ 바닥 인덱스까지 거리) - (중간에 있는 박스 개수)
* 중간에 있는 박스 개수 : A상자의 높이와 같거나 큰 높이 찾기
  
### 완전검색(Exaustive Search)

* 개요
  * 해법으로 생각할 수 있는 모든 경우의 수 나열하고 확인하는 기법
  * **Brute-force** 혹은 **generated-and test 기법**이라고도 불림.
  * 경우의 수 상대적으로 작을 때 유용함.
  * 수행 속도는 느리지만, 해답 찾아내지 못할 확률 작음.
  * 자격검정평가에서 문제 풀이시, 우선 완전 검색으로 접근해 해답 도출 후, 성능 개선 위해 다른 알고리즘 사용해 해답 확인하는 것이 바람직함.
* Baby-gin Game 예제
  * 설명
    * 0~9 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우 run, 동일한 번호를 갖는 경우 triplet이라고 한다.
    * 그리고, 6장의 카드가 run, triplet로만 구성된 경우를 baby-gin이라 한다. (run, run도 가능)
    * 6자의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하다.
    
  * 입력 예
    * 667767 => True
    * 054060 => True
    * 101123 => False
    
  * 완전검색으로 풀이 (조합)
    * 나올 수 있는 모든 경우의 수
    * 3장, 3장씩 그룹으로 나오는 경우의 수. (C(6, 3) * C(3, 3))/2!
    
  * 완전검색으로 풀이 (순열)
  
    * 720가지
  
    * 앞 3장 1그룹, 뒤 3장 2그룹
  
    * 그룹별 3개의 값 같은지, 1씩 커지는지 판단
  
    * 중복순열 생성 예시
  
      ```python
      arr = 'ABC'
      n = len(arr)
      for i in range(n):
          for j in range(n):
              for k in range(n):
                  print(arr[i], arr[j], arr[k])
              	# A A A
                  # A A B
                  # ... (생략)
      ```
  
    * 순열 생성 예시
  
      ```python
      arr = 'ABC'
      n = len(arr)
      for i in range(n):
          for j in range(n):
              if j == i: continue
              for k in range(n):
                  if k == i or k == j continue
                  print(arr[i], arr[j], arr[k])
      ```
  
    * 중첩 for문을 재귀 호출로 구현
  
      * 중첩 for문에서는 i, j, k를 알 수 있음
      * 재귀 호출에서는 알 수 없음 => 전역 변수 or 매개 변수 사용
  
      ```python
      # 나중에..
      ```
  
*  결정 문제
  
  * 답이 2개로 나타낼 수 있는 문제(True or False 등)
* 최적화 문제 (완전 탐색으로 푼다)
  * 최적해를 구하는 문제
  * 최소 혹은 최대가 되는 경우를 찾는다. (외판원 문제)
  * 모든 후보해(가능한 경우)를 조사한다.
  * 순열(n!), 조합, 부분집합(2^n), ...
  * 좀 더 효율적으로 하는 방법이 없을까? (덜 무식하게 완전탐색하는 방법들)
    * 탐색기반 - 백트래킹(그래프, 트리를 탐색하듯이) + (가지치기)
    * 문제간의 관계(재귀적 관계) 동적 계획법 
  * 최적화 문제 중 탐욕 기법으로 풀 수 있는 방법들
    * 쉬운 문제는 풀 수 있지만, 어려운 문제는 대부분 못푼다.
    * Prim, Kruskal
    * 다익스트라
    * 최소비용 신장 트리
  
  

### 탐욕(Greedy) 알고리즘

* 보통 최적해 구하는 데 사용되는 방법

* 지역적으론 최적이지만, 최종적으로 최적일 보장은 없음.

* 거스름돈 줄이기 예시

  * 설명
    * "거스름돈으로 주는 동전의 개수 최소화"
    * 동전 종류 = {500, 100, 50, 10}
    * 거스름 돈 = 800원 
  * 큰 금액의 동전부터 찾고 싶은 해집합에 포함하면서 선택해 나아감.
    * 거스름 돈 = {500}, 300원을 채우는 더 작은 문제로 범위 좁아짐.
    * 거스름 돈 = {500, 500} => -200원. 실행가능 x. 선택 x
    * 거스름 돈 = {500, 100}, 200원
    * 거스름 돈 = {500, 100, 100}, 100원
    * 거스름 돈 = {500, 100, 100, 100}, 0원
  * 완전 탐색 방법은 가능한 거스름 돈 조합 모두.
  * 동전 종류 400원 추가된다면? 동전 종류 = {500, 400, 100, 50, 10}
    * 똑같이 탐욕으로 접근.
    * {500} -> {500, 500} x -> {500, 400} x -> ... -> {500, 100, 100, 100}
    * 이 경우 최적해가 아니다! => 완전 탐색으로 풀어야 함.

* 완전검색이 아닌 탐욕으로 풀어보자!

  * Baby-gin 예시

    * 빈도수 계산해(cnt 배열 사용) 체크
    * 3 이상인 값 => triplet
    * 연속 1이상 => run

    ```python
    num = '456789' # Baby-gin 확인할 6자리 수
    c = [0] * 12 # 6자리 개수 저장할 리스트
    # 0~9 인데 10개가 아닌 12개인 이유 c[i], c[i+1], c[i+2] 비교하려고.
    # 심플하게 하려는 방법, 이렇게 안해도 되긴 함.
    
    # triplete 조사 후 삭제
    # run 조사
    
    # triplet + run == 2이면 Baby-gin!
    ```

    

## 2. 배열 2

### 배열: 2차 배열

* 숫자 퍼즐 예제

* 2차원 배열의 선언

  * list안에 list
  * arr = [[0,1,2,3], [4,5,6,7]]
* **주의**
  
```python
  # 방법 1 - 나의 실수
list1 = [[0] * 3] * 3
  list1[0][0] = 1
  print(list1)
  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
  
  # 방법 2 - 맞는 방법
  list2 = [[0] * 3 for _ in range(3)]
  list2[0][0] = 1
  print(list2)
  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
  ```
  
  * 배열 순회
  
    * n*m개 원소 빠짐없이 조사하는 방법
    * 행 우선순회(첫 번째 행, 두번째 행...)
  
    ```python
    arr = [[1, 2], [3, 4]]
    # python스러운 코드
    for a in arr:
        for val in a:
            print(val)
    ```
  
    * 열 우선순회
  
    * 지그재그 순회
  
    ```python
    # idx 짝수, 홀수일 때로 나눔
    arr = [[1, 2], [3, 4]]
    N = len(arr)
    for i in range(N):
        if not i % 2: # 짝수
            for j in range(N):
                pass
        else:
            for j in range(N-1, -1, -1): # 홀수, N-1부터 0까지
                pass
      
    ```
  
  * 배열의 활용
  
    * 전치 행렬 : 행과 열이 바뀜
    * 대각 순회 i, j = [ 00 => 01 -> 10 => 0, 2 -> 1, 1 -> 2, 0 => ... => 4, 4 ]
  
    ```python
    n, m = len(arr), len(arr[0])
    for diag in range(0, n + m -1) # diag: 사선의 수
    
    # x, y: 시작좌표
    x = 0 if diag < M else (diag - M _1)
    y = diag if diag < M else M -1
    
    while x < n and y >= 0:
        arr[x][y]
        x += 1
        y -= 1
    ```
  
    * 델타를 이용한 2차 배열 탐색
      * 배열의 한 좌표에서 4방향 인접 배열 요소 탐색하는 방법
      * 미로 탐색, 체스 등 많이 쓰임
  
    ```python
    # 상하좌우
    dx = [0, 0, -1, 1] # x 좌표 리스트
    dy = [-1, 1, 0, 0] # y 좌표 리스트
    ```
  
  * 연습문제
  
    * 5*5 2차 배열에 무작위로 25개 숫자로 초기화한 후
    * 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값의 합을 구하시오
    * 주의! 벽에 있는 요소는 이웃한 요소가 없을 수 있음
    * [소스보기](day3_ex1.py)
    * 

### 부분집합 생성(비트)

* 부분집합 합(Subset Sum) 문제

  * n개의 정수로 이루어진 집합이 있을 때, 부분집합 중 집합 원소의 합이 0이 되는 경우가 있는지를 알아내는 문제
  * 결정 문제 (True or False)
  * 최적화 문제로 바꾼다면 '총 합이 0이 되는 경우 중 합이 가장 큰(혹은 작은) 값은?'
  * [-7, -3, -2, 5, 8]이 있을 때, [-3, -2, 5]는 총 합이 0이므로 답이 참이 된다.
  * 완전검색으로 모든 부분집합 생성 후 부분집합 합 구하기

* 부분집합 수 : 2^n개(공집합, 자기자신까지 포함)

  * 각 원소에 대해 포함되거나 되지 않거나 2가지
  * n = 3, {1, 2, 3}, 2^n가지(0~2^n-1)

  |     부분집합      | 2진수 | 10진수 |
  | :---------------: | :---: | :----: |
  |  c(3, 0), 공집합  |  000  |   0    |
  |    c(3, 1) {1}    |  100  |   4    |
  |        {2}        |  010  |   2    |
  |        {3}        |  001  |   1    |
  |  C(3, 2) {1, 2}   |  110  |   6    |
  |      {1, 3}       |  101  |   5    |
  |      {2, 3}       |  011  |   3    |
  | C(3, 3) {1, 2, 3} |  111  |   7    |

  ```python
  arr = 'ABC'
  bits = [0] * 3
  
  for i in range(2):
      bits[0] = i
      for i in range(2):
          bits[1] = i
          for i in range(2):
              bits[2] = i
              print(bits, end = '> ')
              for i in range(len(bits)):
                  if bits[i]: print(arr[i], end=' ')
  # [0, 0, 0]
  # [0, 0, 1]> C
  # ...
  # [1. 1. 1]> A B C
  ```

* 위의 코드 재귀호출로 바꿔보기

```python
arr = 'ABC'
bits = [0] * 3

def subset(k, n):
    if k == n:
        print(bits, end = '> ')
        for i in range(len(bits)):
            if bits[i]: print(arr[i], end=' ')
        
        return
    
    
# 재귀 호출
bits[0] = 0
subset(k + 1, n)
bits[1] = 1
subset(k + 1, n)
            
```

* 비트 연산자 (Bit Operator)

  * &, |, <<, >>, ...

  ```python
  a = 10
  print(bin(10)) # bin() 이진수 표기로 문자형으로 리턴
  
  a = 0b1010
  print(a) # 10진수 표기
  
  # AND 연산
  a = 0b1010
  b = 0b1100
  c = a & b
  print(bin(c)) # => 0b1000
  
  # Shift 연산 << 곱하기, >> 나누기
  print(bin(a << 1)) # => 0b10100
  ```

  * 비트 연산자를 쓰는 이유?

    * 다른 연산에 비해 빠르다. (c에서는 다른 operator보다 적은 명령어)

    ```python
    n = 10
    if n % 2:
        print('홀수')
    else:
        print('짝수')
    
    # 비트 연산자 이용
    n = 10
    if n & 1:
        print('홀수')
    else:
        print('짝수')    
    ```

  * `1 << n`: 2^n

  * `i & (1 << j)`: i의 j번째 비트가 1인지 아닌지를 리턴

* 비트 연산자 사용해 부분집합 생성

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n : 원소의 개수

for i in range(1 << n): # 1 << n: 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
   	print()
print()

```



### 이진 검색 (Binary Search)

* 검색의 종류 : 순차 검색, 이진 검색, 해쉬

* 순차 검색: 브루트 포스 방법

  * 가장 단순하고 직관적인 검색 방법
  * 리스트 등 순차구조로 구현된 자료구조에서 순차적으로 검색
  * 정렬되어 있다면 이진검색을 보통 씀.

* 이진 검색

  * **반드시 정렬된 상태여야 한다.**
  * 중앙에 있는 원소와 비교

  ```python
  def binarySearch(arr, key):
      lo, hi = 0, len(arr)-1
      # lo = 범위의 시작인덱스, hi = 범위의 끝 인덱스
      
      while lo <= hi: # 같아질 때 까지! lo가 커지면 탐색실패!
  		mid = (lo + hi) >> 1 # // 2 (나누기 2)
          if arr[mid] == key:
              return True
          elif arr[mid] > key: # 왼쪽에서 탐색해야함 (lo ~ mid-1)
              hi = mid - 1
          else:
              lo = mid + 1
      return False
  ```

  ```python
  # 재귀호출
  def binarySearch(arr, lo, hi, key):
      if lo > hi: return False
      mid = (lo + hi) >> 1
      if arr[mid] == key:
          return True
      elif arr[mid] > key: # 왼쪽에서 탐색해야함 (lo ~ mid-1)
          return binarySearch(arr, lo, mid - 1, key)
      else:
          return binarySearch(arr, mid + 1, hi, key)
  ```



* 인덱스
  * 대량 데이터 성능 저하 문제 해결 위해 배열 인덱스 사용
  * 문자열의 suffix array(접미사 배열)

### 셀렉션 알고리즘 (Selection Algorithm)

정렬되어 있는(혹은 정렬되지 않은) 자료로부터 k번째로 큰(혹은 작은) 원소를 찾는 방법

### 선택 정렬 (Selection Sort)

k번째 큰값(혹은 작은값) 찾는 것

```python
# 규칙 찾기

arr = [64, 25, 10, 22, 11]
n = len(arr)

# 첫번째 단계 [0, n - 1]
min_idx = 0
for j in range(1, n):
    if arr[min_idx] > arr[j]:
        min_idx = j
arr[0], arr[min_idx] = arr[min_dix], arr[0]

print(arr)

# 두번째 단계 [1, n - 1]
min_idx = 1
for j in range(2, n):
    if arr[min_idx] > arr[j]:
        min_idx = j
arr[1], arr[min_idx] = arr[min_dix], arr[1]

print(arr)
```



```python
# 선택 정렬 코드 

arr = [64, 25, 10, 22, 11]
n = len(arr)

for i in range(n-1): # 범위의 시작 위치 : 0 ~ n-2
    min_idx = i
    for j in range(i+1, n):
        if arr[min_idx] > arr[j]:
        min_idx = j
arr[i], arr[min_idx] = arr[min_dix], arr[i]

print(arr)
```

### 실습 1, 2





## 3. 문자열





## 4. Stack 1





## 5. Stack 2





## 6. Queue





## 7. 연결리스트





## 8. Tree






# APS 응용

그래프, 완전탐색, 분할정복, 백트래킹-BFS, DFS





