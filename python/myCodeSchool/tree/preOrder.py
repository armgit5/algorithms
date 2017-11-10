# https://www.youtube.com/watch?v=gm8DUJJhmY4

from tree import Tree
import sys

def preOrder(root):
    if root == None:
        return None
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return None
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def postOrder(root):
    if root == None:
        return None
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

root = Tree("F")
d = Tree("D")
j = Tree("J")
b = Tree("B")
e = Tree("E")
g = Tree("G")
k = Tree("K")
a = Tree("A")
c = Tree("C")
i = Tree("I")

root.left = d
root.right = j
d.left = b
d.right = e
j.left = g
j.right = k
b.left = a
b.right = c
g.left = i

# preOrder(root)
# inOrder(root)
postOrder(root)