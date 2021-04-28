# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

from node import Node

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.right = two
two.right = five
five.left = three
five.right = six
three.right = four

# Print breathfirst
def levelOrder(root):

    Q = [one]
    s = ''

    while len(Q) != 0:
        current = Q.pop(0)
        s += str(current.info) + ' '
        if current.left:
            Q.append(current.left)
        if current.right:
            Q.append(current.right)

    print(s)

levelOrder(one)

# Q = [1,3,4,6]
# a = Q.pop(0)
# print(Q, a)