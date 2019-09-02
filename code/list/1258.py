# 1258.py 행렬찾기
import sys
sys.stdin = open('1258input.txt', 'r')

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertLast(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def printList(self):
        if self.head is None:
            return

        result = [] # 답
        cur = self.head
        while cur is not None:
            tmp = [cur.row, cur.col]
            result.append(tmp)
            cur = cur.next
        
        result = list(map(str, sorted(result)))
        print(len(result), end=' ')
        print(' '.join(result))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]
    
    mylist = Linkedlist()

    for r in range(n):
        for c in range(n):
            if mymap[r][c] != 0:
                i, j = r, c
                while 0 <= i < n and 0 <= j and mymap[i][j]:
                    mymap[i][j] = 0
                    j += 1
                    if j + 1 < n and mymap[i][j + 1] == 0 or j + 1 == n:
                        i, j = i + 1, c
                ##### 수정하기 끝위치 row, col 찾아서 시작위치부터 끝 위치까지 0으로 바꾸는 함수 짜기
                mylist.insertLast(Node(i, j))
            
    print('#{} '.format(tc), end='')
    mylist.printList()
    

                    
