# deletelast.py
from linkedList import List, Node
print('04.deletelast()_____________\n')

# ------------------------------------------------

mylist = List()
for i in range(1, 6):
    mylist.insertfirst(Node(i))

mylist.deletelast()
mylist.deletelast()
mylist.printlist()
mylist.insertlast(Node(100))
mylist.printlist()

mylist.deletelast()
mylist.deletelast()
mylist.deletelast()
mylist.printlist()
