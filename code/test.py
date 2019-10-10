V, E = 13, 12
L = [0] * (V + 1) # tree = [[0, 0, 0] for _ in range(V + 1)]
R = [0] * (V + 1) # tree = [[] for _ in range(V + 1)]
P = [0] * (V + 1)

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p                # 부모 정보는 필요한 경우에 저장해서 사용

# 1. 트리 순회(전위, 중위, 후위) -----------------------------------------
pre, ino, post = [], [], []
def order(v): # V = 현재 노드
    if v == 0: return
    pre.append(v) # 전위
    order(L[v])
    ino.append(v) # 중위
    order(R[v])
    post.append(v)# 후위
order(1)
print('# 1 - (1). 전위 : {}'.format(*pre))
print('# 1 - (2). 중위 : {}'.format(*ino))
print('# 1 - (3). 후위 : {}'.format(*post))

# 2. 트리의 높이, treeHeight(w) -----------------------------------------
height = 0
def treeHeight(v, curH):
    if v == 0:
        global height
        height = max(height, curH - 1)
        return
    treeHeight(L[v], curH + 1)
    treeHeight(R[v], curH + 1)
treeHeight(1, height)
print('-----------------------------------------')
print('# 2. 트리의 높이 : {}'.format(height))

# 3. 높이가 3인 노드 출력 -----------------------------------------
nodeList = []
def height(v, curH):
    if curH == 3 and v != 0:
        nodeList.append(v)
        return
    if v == 0:
        return
    height(L[v], curH + 1)
    height(R[v], curH + 1)
height(1, 0)
print('-----------------------------------------')
print('# 3. 높이가 3인 노드 : ', end='')
print(*nodeList)

# 4. 트리의 노드 수. treeSize(v): v를 루트로 하는 트리의 노드 수 계산 ---
def treeSize(v):
    if v == 0: return
    global nodeCnt
    nodeCnt += 1
    treeSize(L[v])
    treeSize(R[v])

print('-----------------------------------------')
print('# 4. 트리의 노드 수')
for v in range(1, V + 1):
    nodeCnt = 0
    treeSize(v)
    print('루트가 {}인 트리의 노드 수 : {}'.format(v, nodeCnt))

# 5. 9번, 13번 각각 노드의 조상을 찾아 출력하고, 두 노드의 공통조상 찾아 출력하기
def anc(v): # V = 현재 노드
    tmp = []
    while v != 1:
        tmp.append(P[v])
        v = P[v]
    return tmp
ancList1 = anc(9)
ancList2 = anc(13)
ancList1, ancList2 = sorted(ancList1), sorted(ancList2)
print('-----------------------------------------')
print('# 5 - (1). 노드 9의 조상 : {}'.format(ancList1))
print('# 5 - (2). 노드 13의 조상 : {}'.format(ancList2))
print('# 5 - (3). 9, 13의 공통조상 : ', end='')
x = 0
while ancList1[x] == ancList2[x]:
    print(ancList1[x], end=' ')
    x += 1