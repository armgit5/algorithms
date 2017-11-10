# https://www.youtube.com/watch?v=hmWhJyz5kqc&index=3&list=PLamzFoFxwoNgvI2T5vagi6-wk0Vo8j5OF

from tree import Tree
import sys

def getHeight(root):
    if root == None:
        return -1

    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    return 1 + max(leftHeight, rightHeight)

root = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)
n7 = Tree(7)
n8 = Tree(8)
n9 = Tree(9)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n5.left = n8
n5.right = n9
n3.left = n6
n3.right = n7

print(getHeight(root))
