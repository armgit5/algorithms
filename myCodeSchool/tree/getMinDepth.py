# https://www.youtube.com/watch?v=hmWhJyz5kqc&index=3&list=PLamzFoFxwoNgvI2T5vagi6-wk0Vo8j5OF

from tree import Tree
import sys

def getMinDepth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1

    leftDepth = getMinDepth(root.left) if root.left else sys.maxsize
    rightDepth = getMinDepth(root.right) if root.right else sys.maxsize

    return 1 + min(leftDepth, rightDepth)

root = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)

root.left = n2
root.right = n3
n3.left = n4
n3.right = n5
n4.left = n6

print(getMinDepth(root))
