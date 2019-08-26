# 작업순서 1267.py
# DFS stack1을 사용함
# 유향 그래프
# 시작점 주어지지 않음
# 답을 result stack(stack1과 별도)에 저장해 거꾸로 출력!
# 방문할 때를 기록하지 않고, 더 이상 갈 노드가 없을 때 result stack에 저장한다.
# 방문할 때 기록하는 것은 시작점이 주어진 경우

import sys
sys.stdin = open('1267input.txt', 'r')

def dfs(v):
    tmp_stack = []  # 돌아갈 노드 저장
    tmp_stack.append(v)
    visit[v] = True # 방문

    while tmp_stack: # 재귀 아닐 때 추가, 빈스택이 아닐동안!
        for w in outgoing[v]:
            if not visit[w]: # 방문하지 않은 노드면,
                tmp_stack.append(w)
                visit[w] = True
                v = w
                break
        else: # 갈 노드가 없으면
            result_stack.append(tmp_stack.pop()) # 답 기록!
            if tmp_stack: # 항상 스택 접근할 때 isEmpty 주의한다!
                v = tmp_stack[-1] # 되돌아가기

for tc in range(1, 11):
    v, e = map(int, input().split())
    node = list(map(int, input().split()))

    outgoing = [[] for _ in range(v + 1)] # 나가는 엣지 리스트
    indegree = [0] * (v + 1) # 들어오는 엣지 개수
    visit = [False] * (v + 1) # 방문 여부
    result_stack = [] # 답

    tmp = [160, 137, 172, 140, 119]
    for i in range(e):
        outgoing[node[2 * i]].append(node[2 * i + 1])
        indegree[node[2 * i + 1]] += 1
        if tc == 6:
            if node[2*i] in tmp:
                print(node[2*i], node[2 * i + 1])
    print(indegree)
    a = set()
    b = set()
    for s in range(1, v + 1):
        if indegree[s] == 0:
            a.add(s)
            dfs(s)# DFS 시작
        if indegree[s] == 0 and outgoing[s]:
            b.add(s)
    if tc==6:
        print(a)
        print(b)
        print(a - b)
    # print(a - b)

    # if tc == 6:
    #     for t in tmp:
    #         print(outgoing[t], indegree[t])
    print(v)
    print(len(result_stack))
    result_stack = list(map(str, reversed(result_stack)))
    print('#{} {}'.format(tc, ' '.join(result_stack)))

'''
def DFS(v):
    visit[v] == True
    result.append(v)

    for w in adj[v]:
        if not visit[w]:
            DFS(w)




    for i in range(1, v + 1):
        if not comein[i] and adj[i]: # 들어오는 간선 없고, 나가는 간선 있는 경우
            start = i
            break

    DFS(start)
    result = list(map(str, result))
    print('#{} {}'.format(tc, ' '.join(result)))

'''