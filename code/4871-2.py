# 그래프 경로 4871.py
# 유향 그래프
# stack을 사용한 DFS
################# runtime error! 미완성코드
import sys
sys.stdin = open('4871input.txt', 'r')

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

    result = DFS(s, g) # 1: 존재, 0: 존재 x
    print('#{} {}'.format(tc, result))