# https://www.geeksforgeeks.org/floor-in-binary-search-tree-bst/

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def floor_bst(root, num):
    if root == None:
        return 1000000 # return highest because looking for floor

    if num == root.data:
        return num

    #  Left subtree
    if root.data > num:
        return floor_bst(root.left, num)

    # Right subtree
    floor_value = floor_bst(root.right, num)

    if floor_value <= num:
        return floor_value
    else:
        return root.data

def ceil_bst(root, num):
    if root == None:
        return -1000000 # return highest because looking for floor

    if num == root.data:
        return num

    if root.data < num:
        return ceil_bst(root.right, num)

    ceil_value = ceil_bst(root.left, num)

    if ceil_value >= num:
        return ceil_value
    else:
        return root.data


ten = Node(10)
five = Node(5)
fifteen = Node(15)
twelve = Node(12)
thirty = Node(30)

ten.left = five
ten.right = fifteen
fifteen.left = twelve
fifteen.right = thirty

print(floor_bst(ten, 16))
print(ceil_bst(ten, 16))