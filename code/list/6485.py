# 6485.py 삼성시의 버스 노선


import sys
sys.stdin = open('6485input.txt', 'r')

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertLast(self, node):
        if self.head is None: # 빈리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def findStation(self, c):
        cnt = 0
        if self.head is None: # 빈 리스트
            return cnt

        cur = self.head
        while cur is not None:
            if cur.start <= c <= cur.end:
                cnt += 1
            cur = cur.next

        return cnt

t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    mylist = LinkedList()
    for i in range(n):
        start, end = map(int, input().split())
        mylist.insertLast(Node(start, end))

    print('#{}'.format(tc), end='')
    p = int(input())
    for i in range(p):
        c = int(input())
        print(' {}'.format(mylist.findStation(c)), end='')
    print()
