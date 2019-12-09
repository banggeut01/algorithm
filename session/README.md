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
  * [코드](./2667.py)

* 2468.안전영역

  * [문제](https://www.acmicpc.net/problem/2468)

  * [코드](./2468.py)

  * 런타임 에러

    - python3으로 제출하기

      ```python
      import sys
      sys.setrecursionlimit(10000)
      ```

  * 틀렸습니다

    * 아무 지역도 물에 잠기지 않을 수도 있다. -> 비가 오지 않는 경우도 고려해야한다.
    * 안전영역의 개수는 최소 1개이다.

* 2636.치즈
  * [문제](https://www.acmicpc.net/problem/2636)
  * [코드](./2636.py)
  * 런타임 에러
    * python3, recursionlimit 10000

* 2573.빙산
  * [문제](https://www.acmicpc.net/problem/2573)
  * [코드](./2573.py)

* 2589.보물섬
  * [문제]
  * [코드]

* 16234.인구이동
  * [문제]
  * [코드]

# 조합 탐색, 백트래킹

* 14502.연구소
  * [문제]
  * [코드]

* 14889.스타트와 링크
  * [문제]
  * [코드]

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