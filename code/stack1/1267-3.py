# 작업순서 1267-3.py
# DAG 사용
# Queue, indegree 사용

from collections import deque
import sys
sys.stdin = open('1267input.txt', 'r')

def dag():
    v = queue[0]
    while queue:
        for w in outgoing[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
        result.append(queue.popleft())
        if len(queue) != 0: v = queue[0]

for tc in range(1, 11):
    v, e = map(int, input().split())
    node = list(map(int, input().split()))

    outgoing = [[] for _ in range(v + 1)] # 나가는 엣지 리스트
    indegree = [0] * (v + 1) # 들어오는 엣지 개수
    # visit = [False] * (v + 1) # 방문 여부
    result = [] # 답, 위상순서
    queue = deque()

    for i in range(e):
        outgoing[node[2 * i]].append(node[2 * i + 1])
        indegree[node[2 * i + 1]] += 1 


    for s in range(1, v + 1):
        if indegree[s] == 0: # 시작노드!
            queue.append(s)
    
    dag()

    result = list(map(str, result))
    print('#{} {}'.format(tc, ' '.join(result)))
