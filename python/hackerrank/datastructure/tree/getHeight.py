# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def height(root):
    if root == None:
        return -1

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1 + max(leftHeight, rightHeight)

tree = BinarySearchTree()
tree.create(3)
tree.create(5)
tree.create(2)
tree.create(1)
tree.create(4)
tree.create(6)
tree.create(7)

print(height(tree.root))