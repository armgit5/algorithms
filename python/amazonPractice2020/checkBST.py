# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_r=next-challenge&h_v=zen

import sys

class Node():
    def __init__(self, id):
        self.data = id
        self.left = None
        self.right = None

# check this why this is wrong https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
def checkBST(root):
    if root == None:
        return True

    l = checkBST(root.left)

    if root.left != None and root.left.data > root.data:
        return False

    if root.right != None and root.right.data < root.data:
        return False

    r = checkBST(root.right)

    return l and r

# min max
# or use in order to compare if current < prev data
def isBSTHelper(root, min, max):
    if root == None:
        return True

    if root.data < min or root.data > max:
        return False

    l = isBSTHelper(root.left, min, root.data - 1)
    r = isBSTHelper(root.right, root.data + 1, max)

    return l and r

def isBST(root):
    return isBSTHelper(root, -sys.maxsize, sys.maxsize)


# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

# # Set 1 test pass
# four.left = two
# four.right = six
# two.left = one
# two.right = three
# six.left = five
# six.right = seven

# Set 2 test fail
three.left = two
three.right = five
two.left = one
two.right = four


# print(checkBST(four))
print(isBST(three))
