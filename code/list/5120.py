# 5120.py 암호
import sys
sys.stdin = open('5120input.txt', 'r')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head is None:
            print('빈리스트')
            return

        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def insertLast(self, node):
        if self.head is None: #빈리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertAt(self, idx, k): # idx:삽입위치, k:반복횟수
        if self.head is None:
            return

        # 삽입 위치 찾기
        prev, cur = None, self.head
        for _ in range(k):
            i = idx
            while i > 0:
                if cur is None: # 리스트 끝
                    cur = self.head
                prev = cur
                cur = cur.next
                i -= 1

            if prev is None: # 첫번째
                node = Node(cur.data + self.tail.data)
                self.head = node
                node.next = cur
                cur = self.head
            elif cur is None: # 마지막
                node = Node(self.head.data + prev.data)
                self.tail.next = node
                self.tail = node
                cur = self.tail
            else:
                node = Node(cur.data + prev.data)
                prev.next = node
                node.next = cur
                cur = prev.next

    def printListReverse(self):
        if self.head is None:  # 빈리스트
            print('빈리스트')
            return

        cur, tmp = self.head, []
        while cur is not None:
            tmp.append(cur.data)
            cur = cur.next

        for i in range(1, 11):
            if len(tmp) < i:
                break
            print(tmp[-i], end=' ')
        print()



t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split()) # n: 수열크기, m: 삽입 위치, k: 반복 횟수
    inputs = list(map(int, input().split()))

    mylist = LinkedList()
    # 리스트 생성
    for data in inputs:
        mylist.insertLast(Node(data))

    mylist.insertAt(m, k)

    print('#{} '.format(tc), end='')
    mylist.printListReverse()

