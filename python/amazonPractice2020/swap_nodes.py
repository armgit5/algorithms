# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

from node import Node

# indexes = [[2, 3], [-1, -1], [-1, -1]]
# queries = [1, 1]

indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
queries = [2, 3]

# indexes = [[-1, 2], [-1, 3], [-1, 4], [-1, 5], [-1, 6]]
# queries = [2, 689]
# indexes = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
# queries = [2, 4]

# indexes = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
# queries = [2]


s = ''
def inorder_print(root):
    global  s

    if root == None:
        return

    inorder_print(root.left)
    s += str(root.info) + ' '
    inorder_print(root.right)

def make_tree(indexs, root):
    Q = [root]

    for i in indexes:
        current = Q.pop(0)
        if i[0] != -1:
            current.left = Node(i[0])
            Q.append(current.left)
        if i[1] != -1:
            current.right = Node(i[1])
            Q.append(current.right)

def swap_helper(node):
    tmp_node = None
    if node.left:
        tmp_node = node.left
        node.left = node.right
        node.right = tmp_node
    else:
        tmp_node = node.right
        node.right = node.left
        node.left = tmp_node

def swapNodes(indexes, queries):

    root = Node(1)
    make_tree(indexes, root)

    # walk each level
    Q = []

    global s
    output = []

    # Loop through queries
    for height in queries:
        Q.append(root)
        current_height = 1
        # loop through Q
        while len(Q) > 0:
            # loop through nodes in current Q
            for _ in range(len(Q)):
                current = Q.pop(0)

                if current_height % height == 0:
                    swap_helper(current)

                if current.left:
                    Q.append(current.left)
                if current.right:
                    Q.append(current.right)

            current_height += 1

        inorder_print(root)
        output.append(s)
        s = ''

    return output

result = swapNodes(indexes, queries)
# result = ['123', '312']
print('\n'.join([''.join(map(str, x)) for x in result]))