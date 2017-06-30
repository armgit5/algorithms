# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

"""
5
3 0
5 1
4 2
2 3
10 1
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def insertNth(head, data, position):
    newNode = Node(data)
    # print(position, head, data)
    if head == None:
        return newNode
    if position == 0:
        newNode.next = head
        return newNode

    current = head

    for _ in range(position - 1):
        current = current.__next__

    newNode.next = current.__next__
    current.next = newNode

    return head

def printNodes(head):
    current = head
    print((current.data))
    while current.__next__:
        current = current.__next__
        print((current.data))

head = None
head = insertNth(head, 3, 0)
head = insertNth(head, 5, 1)
head = insertNth(head, 4, 2)
head = insertNth(head, 2, 3)
head = insertNth(head, 10, 1)
printNodes(head)