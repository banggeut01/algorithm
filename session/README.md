# 계절학기 - 알고리즘 A형

>  7일(하루 4시간)동안 진행되는 계절학기!

# 탐색 - BFS, DFS

> 너비 우선 탐색
>
> 기본적인 그래프 탐색(결합 컴포넌트를 찾을 때)
>
> 최단 경로를 찾을 때 DFS 보다 유리(간선의 가중치가 없는 경우)
>
> D[v] = D[u] + 1



> 가중치가 부여되어 있다면 -> 간선 완화를 적용
>
> (u, v) 간선에 대한 완화 과정
>
> D[]: 시작점에서 최단 경로의 가중치 합
>
> if D[v] > D[u]  + weight(u, v):
>
> ​	D[v] = D[u]  + weight(u, v)

```python
import collections
def BFS(v):
    # 큐 생성하고 시작점을 큐에 삽입하고 방문표시
    Q = collections.deque()
    Q.append(s); visit[s] = 1; D[s] = 0;
    # 빈큐가 아닐동안 반복해서
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visit[v]:
                visit[v] = 1
                Q.append(v)
                D[v] = D[u] + 1
    
V, E = map(int, input().split()) 
G = [[] for _ in range(V + 1)] # 인접 리스트
visit = [0] * (V + 1) # 정점의 수 만큼

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(v) # 인접 리스트
```



* 2667.단지번호붙이기
  * [문제](https://www.acmicpc.net/problem/2667)
  
* [코드](./2667.py) (BFS)
  
  * DFS로 풀었을 때 return value
  
    ```python
    def DFS(x, y):
        ret = 1 # x,y좌표 집 1개
        for dx, dy in (-1, 0), ...:
            nx, ny = x + dx, y + dy
            if 조건...:
                ret += DFS(nx, ny)
        return ret
    ```
  
  * 재귀 함수 트리 이해하기
  
    ```python
    def backtrack(k, n):
        if k == n: return 1
        
        ret = 0
        ret += backtrack(k + 1, n)
        ret += backtrack(k + 1, n)
        
        return ret
    
    backtrack(0, 3)
    ```
  
    ```python
    def backtrack(k, n):
        global cnt
        if k == n: 
            cnt += 1
            return
        
        ret += backtrack(k + 1, n)
        ret += backtrack(k + 1, n)
    
    cnt = 0
    backtrack(0, 3)
    print(cnt)
    ```
  
    * 트리는 싸이클이 없기 때문에 방문 표시할 필요 없다.
  
    * 단말 노드인지 아닌지만 체크하면 된다.
  
    * 그래프 탐색시 BFS로 방문 표시
  
    * 트리 탐색시 단말노드인지 아닌지 체크
  
* 2468.안전영역

  * [문제](https://www.acmicpc.net/problem/2468)

  * [코드](./2468.py)

  * 런타임 에러

    - python3으로 제출하기

      ```python
      import sys
      sys.setrecursionlimit(10000)
      ```
      
    - 시험에선 sys 못쓴다.

    - 시험장에선 recursionlimit 설정해놓았을 것. 걱정 노노!

    - 불안하면 BFS로 돌리기!

  * 틀렸습니다

    * 아무 지역도 물에 잠기지 않을 수도 있다. -> 비가 오지 않는 경우도 고려해야한다.
    * 안전영역의 개수는 최소 1개이다.
    
  * 보완점

    * 최고 비높이 maxH를 구해준 것 처럼 minH를 구해 시간을 줄일 수 있다.

* 2636.치즈
  * [문제](https://www.acmicpc.net/problem/2636)
  * [코드](./2636.py)
  * 런타임 에러
    * python3, recursionlimit 10000

* 2573.빙산
  * [문제](https://www.acmicpc.net/problem/2573)
  * [코드](./2573.py)
* 런타임에러
    * DFS가 아닌 BFS로 풀어보기! 
    * 최대 10,000개의 칸이 있을 수 있기 때문에 재귀 오류
  
* 2589.보물섬
  * [문제](https://www.acmicpc.net/problem/2589)
  * [코드](./2589.py)

* 16234.인구이동
  * [문제](https://www.acmicpc.net/problem/16234)
  * [코드](./16234.py)
  * [런타임에러 DFS 코드](./16234_fail.py)

# 조합 탐색, 백트래킹

* 14502.연구소
  * [문제]
  * [코드]

* 14889.스타트와 링크
  * [문제](https://www.acmicpc.net/problem/14889)
  * [코드](./14889.py)

* 15686.치킨배달
  * [문제]
  * [코드]

* 17471.게리맨더링
  * [문제]
  * [코드]

* 17070.파이프 옮기기1
  * [문제]
  * [코드]

* 17135.캐슬디펜스
  * [문제]
  * [코드]

* 14501.퇴사
  * [문제]
  * [코드]
* 14888.연산자끼워넣기
  * [문제]
  * [코드]
* 15683.감시
  * [문제]
  * [코드]