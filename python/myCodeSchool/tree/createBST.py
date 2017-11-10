# https://www.youtube.com/watch?v=VCTP81Ij-EM&index=2&list=PLamzFoFxwoNgvI2T5vagi6-wk0Vo8j5OF&t=30s
# create BST from array

from tree import Tree
from tree import isBinarySearchtree
from tree import to_string

a = [1,2,3,4,5,6,7,8,9]

def createBST(a, start, end):

    if start > end:
        return None

    mid = int((start + end) / 2)

    root = Tree(a[mid])

    root.left = createBST(a, start, mid-1)
    root.right = createBST(a, mid+1, end)

    return root

root = createBST(a, 0, len(a)-1)

print(isBinarySearchtree(root))
to_string(root)
