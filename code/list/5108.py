# 5108.py 숫자 추가

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
            print('빈 리스트')
            return
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next
            print()

    def insertLast(self, node):
        if self.head is None: # 빈리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertAt(self, idx, data):
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
            return

        prev, cur = None, self.head # 이전노드, 현재노드
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째위치에 삽입
            node.next = cur
            self.head = node
        elif cur is None: # 마지막 위치에 삽입
            prev.next = node
            self.tail = node
        else:
            prev.next = node
            node.next = cur

    def printAt(self, idx):
        if self.head is None:
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            cur = cur.next
            idx -= 1

        if cur is None: # 원소 개수 초과시 마지막 원소 출력
            return prev.data
        else:
            return cur.data

t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split()) # n: 수열길이, m: 추가 횟수, l: 출력할 인덱스 번호
    inputs = list(map(int, input().split()))

    mylist = LinkedList()
    for data in inputs:
        mylist.insertLast(Node(data))

    for _ in range(m):
        idx, data = map(int, input().split())
        mylist.insertAt(idx, data)
        # mylist.printList()

    print('#{} {}'.format(tc, mylist.printAt(l)))

