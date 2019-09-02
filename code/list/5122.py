# 5122.py 수열 편집
import sys
sys.stdin = open('5122input.txt', 'r')

class Node:
    def __init__(self, data):
        self.data = data
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

    def printList(self):
        if self.head is None:
            print('빈리스트')
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next

            print()

    def insertAt(self, idx, node):
        if self.head is None: # 빈리스트
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째위치에 추가
            node.next = self.head
            self.head = node
        elif cur is None: # 마지막위치에 추가
            self.tail.next = node
            self.tail = node
        else:
            prev.next = node
            node.next = cur

    def updateAt(self, idx, data):
        if self.head is None: # 빈리스트
            return

        cur = self.head
        while idx > 0 and cur is not None:
            cur = cur.next
            idx -= 1

        cur.data = data

    def deleteAt(self, idx):
        if self.head is None: # 빈리스트
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째위치
            self.head = cur.next
        elif cur is None: # 마지막위치
            prev.next = None
            self.tail = prev
        else:
            prev.next = cur.next

    def printAt(self, idx):
        if self.head is None:  # 빈리스트
            return -1

        cur = self.head
        while idx > 0 and cur is not None:
            cur = cur.next
            idx -= 1

        if cur is None: 
            if idx == 0:# 마지막위치
                return self.tail.data
            else:
                return -1
        else:
            return cur.data


t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split()) # n: 수열길이, m: 추가횟수, l: 출력인덱스번호
    inputs = list(map(int, input().split()))

    # 연결리스트 생성
    mylist = LinkedList()
    for data in inputs:
        mylist.insertLast(Node(data))

    for _ in range(m):
        inputs = list(input().split())
        if inputs[0] == 'I': # 추가
            mylist.insertAt(int(inputs[1]), Node(int(inputs[2]))) # idx, node
        else:
            if inputs[0] == 'C': # 수정
                mylist.updateAt(int(inputs[1]), int(inputs[2])) # idx, node
            else: # 삭제
                mylist.deleteAt(int(inputs[1])) # idx

    print('#{} {}'.format(tc, mylist.printAt(l)))