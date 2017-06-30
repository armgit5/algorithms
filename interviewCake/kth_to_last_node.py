# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


"""
O(n) time and O(1)O(1) space, where nn is the length of the list.

More precisely, it takes nn steps to get the length of the list, and another n-kn−k steps to reach the target node.
In the worst case k=1k=1, so we have to walk all the way from head to tail again to reach the target node. 
This is a total of 2n2n steps, which is O(n)O(n).
"""

def kth_to_last_node(pos, a):
    node_length = 1
    current = a

    while current.next:
        node_length += 1
        current = current.next

    travel = node_length - pos

    current = a
    for _ in range(travel):
        current = current.next
    print(current.value)

def kth_to_last_node_stick(pos, a):
    node_length = 1
    left = a
    right = a

    for _ in range(pos - 1):
        right = right.next

    while right.next:
        left = left.next
        right = right.next

    print(left.value)

kth_to_last_node(2, a)
kth_to_last_node_stick(2, a)