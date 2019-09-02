# 1258.py 행렬찾기
import sys
sys.stdin = open('1258input.txt', 'r')

class Node:
    def __init__(self, size, row, col):
        self.size = size
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
            tmp = [cur.size, cur.row, cur.col]
            result.append(tmp)
            cur = cur.next
        
        result = sorted(result)
        print(len(result), end='')
        for i in range(len(result)):
            print(' {} {}'.format(result[i][1], result[i][2]), end='')
        print()

def updateMap(i, j, n, m):
    for row in range(i, n):
        for col in range(j, m):
            mymap[row][col] = 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]
    
    mylist = Linkedlist()

    for r in range(n):
        for c in range(n):
            if mymap[r][c] != 0:
                i, j = r, c
                while 0 <= j < n and mymap[i][j]:
                    j += 1
                while 0 <= i < n and mymap[i][j - 1]:
                    i += 1
                updateMap(r, c, i, j) # r,c: 시작 위치, i,j: 끝 위치 + 1
                mylist.insertLast(Node((i - r) * (j - c), i - r, j - c))
            
    print('#{} '.format(tc), end='')
    mylist.printList()
    

                    
