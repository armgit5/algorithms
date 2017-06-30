# https://www.youtube.com/watch?v=NBcqBddFbZw&t=15s&index=1&list=PLamzFoFxwoNgvI2T5vagi6-wk0Vo8j5OF

from tree import Tree

def getLCA(curr, A, B):

    if curr == None:
        return None

    if curr.data == A or curr.data == B:
        return curr

    left = getLCA(curr.left, A, B)
    right = getLCA(curr.right, A, B)

    if left != None and right != None:
        return curr

    if left == None:
        return right
    else:
        return left


root = Tree(1, Tree(2, Tree(4), Tree(5, Tree(7), Tree(8))), Tree(3))
node = getLCA(root, 2, 4)
print(node.data)