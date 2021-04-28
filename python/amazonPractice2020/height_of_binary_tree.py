# https://www.youtube.com/watch?v=_pnqMz5nrRs
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# recursive find left subtree or right subtree + 1

from node import BinarySearchTree

arr = [3, 5, 2, 1, 4, 6, 7]

tree = BinarySearchTree()
for i in range(len(arr)):
    tree.create(arr[i])

def height(root):

    if (root == None):
        return -1

    # call left subtree
    l = height(root.left)
    # call right subtree
    r = height(root.right)

    # return max height
    return max(l, r) + 1

print(height(tree.root))