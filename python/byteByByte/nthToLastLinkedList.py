# https://www.youtube.com/watch?v=i7v1UWlaYrI&index=2&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def nthToLast(node, n):
    curr = node
    follower = node

    # Move curr n steps further
    for i in range(n):
        if curr == None:
            return None
        curr = curr.next

    # If len is n, then return None
    if curr == None: return None

    # Find the last element and return follower
    while curr.next != None:
        curr = curr.next
        follower = follower.next

    return follower


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five

node = nthToLast(one, 6)
if node != None: print(node.value)

