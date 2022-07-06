class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval= None


class SLinkedList:
    def __init__(self):
        self.headval = None

lst1 = SLinkedList()
lst1.headval = Node("Mone")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Tues")
e5 = Node("Fr")
lst1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5