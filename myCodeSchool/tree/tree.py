import sys

class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isBinarySearchtreeHelper(root, minValue, maxValue):

    if root == None: return True

    if root.data > minValue and \
        root.data < maxValue and \
        isBinarySearchtreeHelper(root.left, minValue, root.data) and \
        isBinarySearchtreeHelper(root.right, root.data, maxValue):
        return True
    else:
        return False

def isBinarySearchtree(root):
    return isBinarySearchtreeHelper(root, -sys.maxsize, sys.maxsize)

def to_string(root):
    if root == None: return root
    print((root.data))
    to_string(root.left)
    to_string(root.right)