# https://www.youtube.com/watch?v=UQfr5cNnvzA&index=43&list=PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE

from tree import Tree, to_string

def toSumTree(node):
    if node == None:
        return 0

    # Store old value
    oldVal = node.data

    # Set current node data
    node.data = toSumTree(node.left) + toSumTree(node.right)

    return oldVal + node.data

'''
        10                          20(4-2 + 12+6)
    -2      6       ->     4(8-4)         12(7+5)
  8    -4 7   5          0      0      0         0
'''
tree = Tree(10)
tree.left = Tree(-2)
tree.right = Tree(6)
tree.left.left = Tree(8)
tree.left.right = Tree(-4)
tree.right.left = Tree(7)
tree.right.right = Tree(5)

to_string(tree)

print("")
toSumTree(tree)

to_string(tree)
