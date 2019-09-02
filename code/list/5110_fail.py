# 5110_fail.py 수열 합치기
# 제한 횟수 초과 에러

import sys
sys.stdin = open('5110input.txt', 'r')

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        # self.rvs_next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        # self.rvs_head = None
        # self.rvs_tail = None

    def printList(self):
        if self.head is None:
            print('빈리스트')
            return

        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def findIdx(self, data):
        if self.head is None: # 빈 리스트
            return 0

        cur, idx = self.head, 0
        while cur is not None:
            if cur.data <= data:
                cur = cur.next
                idx += 1
            else:
                return idx

        if cur is None:
            return idx

        if self.head == cur:
            return 0

    def insertAt(self, idx, node):
        if self.head is None: # 빈리스트
            self.head = self.tail = node
            # self.rvs_head = self.rvs_tail = node
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째 위치에 삽입
            node.next = cur
            self.head = node
            # self.rvs_tail = node
            # cur.rvs_next = node

        elif cur is None: # 마지막 위치에 삽입
            prev.next = node
            self.tail = node
            # node.rvs_next = prev
            # self.rvs_head = node
        else:
            prev.next = node
            node.next = cur
            # cur.rvs_next = node
            # node.rvs_next = prev

    def printListReverse(self):
        if self.head is None:  # 빈리스트
            print('빈리스트')
            return

        cur, tmp = self.head, []
        while cur is not None:
            tmp.append(cur.data)
            cur = cur.next

        result = list(reversed(tmp))
        print(' '.join(list(map(str, result[:10]))))

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split()) # n: 수열 길이, m: 수열 개수
    mylist = LinkedList()

    for _ in range(m):
        inputs = list(map(int, input().split()))
        pos = mylist.findIdx(inputs[0])
        for i in range(n):
            node = Node(inputs[i])
            mylist.insertAt(pos + i, node)
        # mylist.printList()

    # print('#{} {}'.format(tc, printListReverse()))
    print('#{}'.format(tc), end=' ')
    # mylist.printList()
    mylist.printListReverse()

    '''
        def printListReverse(self):
            if self.head is None: # 빈리스트
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
    '''

    '''
    def printListReverse(self):
        if self.head is None: # 빈리스트
            print('빈리스트')
            return

        cur, cnt = self.rvs_head, 0
        while cnt < 10 and cur is not None:
            print(cur.data, end=' ')
            cur = cur.rvs_next
            cnt += 1
        print()
    '''