# deleteAt.py
from linkedList import List, Node
print('07.deleteAt()_____________\n')
# ------------------------------------------------

mylist = List()
for i in range(1, 6):
    mylist.insertfirst(Node(i))

mylist.printlist()

print('2 위치를 삭제하자')
mylist.deleteAt(2)
mylist.printlist()

print('4 위치를 삭제하자')
mylist.deleteAt(4)
mylist.printlist()

print('3 위치를 삭제하자')
mylist.deleteAt(3)
mylist.printlist()

