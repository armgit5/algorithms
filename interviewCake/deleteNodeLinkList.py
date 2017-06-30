class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def string(a):
    temp = a
    print((temp.value))
    while temp.__next__:
        print((temp.next.value))
        temp = temp.__next__

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(b):

    if b.__next__:

        b.value = b.next.value
        b.next = b.next.__next__
    else:
        b = None
        b.next = None

string(a)
delete_node(b)
string(a)