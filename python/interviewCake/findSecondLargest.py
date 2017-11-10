# https://www.interviewcake.com/question/python/second-largest-item-in-bst?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email

'''

      ( 5 )
        /     \
      (3)     (8)
     /  \     /  \
   (1)  (4) (7)  (12)
                 /
               (10)
               /  \
             (9)  (11)

   O(h) space and O(h) time
'''
def find_largest(root_node):
    if root_node is None:
        raise Exception('Tree must have at least 1 node')
    if root_node.right is not None:
        return find_largest(root_node.right)
    return root_node.value

def find_second_largest(root_node):
    if root_node is None or \
            (root_node.left is None and root_node.right is None):
        raise Exception('Tree must have at least 2 nodes')

    # case: we're currently at largest, and largest has a left subtree,
    # so 2nd largest is largest in said subtree
    if root_node.left and not root_node.right:
        return find_largest(root_node.left)

    # case: we're at parent of largest, and largest has no left subtree,
    # so 2nd largest must be current node
    if root_node.right and \
       not root_node.right.left and \
       not root_node.right.right:
        return root_node.value

    # otherwise: step right
    return find_second_largest(root_node.right)

'''O(1) space O(h) time'''

def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_second_largest(root_node):
    if root_node is None or \
            (root_node.left is None and root_node.right is None):
        raise Exception('Tree must have at least 2 nodes')

    current = root_node

    while current:
        # case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if current.right and \
           not current.right.left and \
           not current.right.right:
            return current.value

        current = current.right