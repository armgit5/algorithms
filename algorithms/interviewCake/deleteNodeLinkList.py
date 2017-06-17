class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def string(a):
    temp = a
    print temp.value
    while temp.next:
        print temp.next.value
        temp = temp.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(b):

    if b.next:

        b.value = b.next.value
        b.next = b.next.next
    else:
        b = None
        b.next = None

string(a)
delete_node(b)
string(a)