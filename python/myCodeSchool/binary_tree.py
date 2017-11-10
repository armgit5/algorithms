import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root == None:
           self.root = Node(new_val)
        else:
            self.insert_helper(self.root, new_val)

    def insert_helper(self, root, new_val):
        if new_val < root.value:
            if root.left:
                self.insert_helper(root.left, new_val)
            else:
                root.left = Node(new_val)
        else:
            if root.right:
                self.insert_helper(root.right, new_val)
            else:
                root.right = Node(new_val)


    def search(self, find_val):

        if self.root:
            return self.preorder_search(self.root, find_val)

        return False

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        if start:
            if start.value == find_val:
                return True
            elif find_val < start.value:
                return self.preorder_search(start.left, find_val)
            elif find_val > start.value:
                return self.preorder_search(start.right, find_val)
        return False

    def findMin(self, root):
        while root.left != None:
            root = root.left
        return root

    def delete(self, root="root", data=None):

        if root == "root": root = self.root
        if root == None: return root


        elif data < root.value: root.left = self.delete(root.left, data)
        elif data > root.value: root.right = self.delete(root.right, data)
        else:
            # case 1 no child
            if root.left == None and root.right == None:
                root = None

            # case 2
            elif root.left == None:
                temp = root
                root = root.right
                temp = None

            elif root.right == None:
                temp = root
                root = root.left
                temp = None

            # case 3: 2 children
            else:
                temp = self.findMin(root.right)
                # print temp.value
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)
                temp = None
        return root

    def find(self, find_val):

        if self.root:
            return self.preorder_find(self.root, find_val)

        return None

    def preorder_find(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        if start:
            if start.value == find_val:
                return start
            elif find_val < start.value:
                return self.preorder_find(start.left, find_val)
            elif find_val > start.value:
                return self.preorder_find(start.right, find_val)
        return None

    def in_order_successor(self, data):
        current = self.find(data)
        if current == None:
            return None

        # case 1: node has right subtree
        print(current)
        if current.right != None:
            return self.findMin(current.right)

        # case 2: no right subtree
        successor = None
        ancestor = self.root
        while ancestor != current:
            if current.value < ancestor.value:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor

    def to_string(self, root="root"):
        if root == "root": root = self.root
        if root == None: return root
        print((root.value))
        self.to_string(root.left)
        self.to_string(root.right)


def isBinarySearchtreeHelper(root, minValue, maxValue):

    if root == None: return True

    if root.value > minValue and \
        root.value < maxValue and \
        isBinarySearchtreeHelper(root.left, minValue, root.value) and \
        isBinarySearchtreeHelper(root.right, root.value, maxValue):
        return True
    else:
        return False

def isBinarySearchtree(root):
    return isBinarySearchtreeHelper(root, -sys.maxsize, sys.maxsize)

# # Set up tree
# tree = BST(7)
#
# # Insert elements
# tree.insert(4)
# tree.insert(9)
# tree.insert(1)
# tree.insert(6)

# Set up tree
tree = BST(12)

# Insert elements
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(15)
tree.insert(13)
tree.insert(17)



# print isBinarySearchtree(tree.root)

# tree.delete("root", 15)
# tree.to_string("root")

print((tree.in_order_successor(5).value))

