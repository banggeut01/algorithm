# linkedList.py 연결 리스트 실습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None: # 공백 리스트인지 체크
            return
        cur = self.head # cur: 현재 노드
        print('[', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, node):
        if self.head is None: # 빈 리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None:
            return

        prev, cur = None, self.head # 이전노드, 현재노드
        while cur.next is not None: # while 후 cur 가 마지막 노드를 가리키게 됨
            prev = cur
            cur = cur.next

        if prev is None: # if self.size == 1: 노드 1개 일 때,
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev

        del cur
        self.size -= 1

    def deletefirst(self):
        if self.head is None:
            return
        cur = self.head
        if self.head == self.tail: # 1개
            self.head = self.tail = None
        else:
            self.head = cur.next

        del cur
        self.size -= 1



    def insertAt(self, idx, node): # idx : 삽입 위치, node : 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next 
                idx -= 1

            if prev is None: # 첫번째 위치에 삽입
                node.next = cur
                self.head = node
            elif cur is None: # 범위 벗어나 마지막 위치에 삽입
                prev.next = self.tail = node
            else:
                node.next = cur
                prev.next = node

            self.size += 1
    def deleteAt(self, idx):
        if self.head is None: # 빈 리스트
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째 위치 삭제
            self.head = cur.next
        elif cur is None: # 마지막 위치 삭제
            self.tail = prev
        else:
            prev.next = cur.next

        del cur
        self.size -= 1