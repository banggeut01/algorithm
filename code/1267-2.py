# 작업순서 1267-2.py
# DFS 재귀를 사용함
# 유향 그래프
# 시작점 주어지지 않음
# 답을 result stack에 저장해 거꾸로 출력!
# 방문할 때를 기록하지 않고, 더 이상 갈 노드가 없을 때 result stack에 저장한다.
# 방문할 때 기록하는 것은 시작점이 주어진 경우

import sys
sys.stdin = open('1267input.txt', 'r')

def dfs(v):
    visit[v] = True # 방문

    for w in outgoing[v]:
        if not visit[w]:
            dfs(w)
    
    result_stack.append(v) # 더 이상 갈 노드가 없을 때!


for tc in range(1, 11):
    v, e = map(int, input().split())
    node = list(map(int, input().split()))

    outgoing = [[] for _ in range(v + 1)] # 나가는 엣지 리스트
    indegree = [0] * (v + 1) # 들어오는 엣지 개수
    visit = [False] * (v + 1) # 방문 여부
    result_stack = [] # 답

    for i in range(e):
        outgoing[node[2 * i]].append(node[2 * i + 1])
        indegree[node[2 * i + 1]] += 1 

    for s in range(1, v + 1):
        if indegree[s] == 0: # 시작노드!
            dfs(s)# DFS 시작

    result_stack = list(map(str, reversed(result_stack)))
    print('#{} {}'.format(tc, ' '.join(result_stack)))
