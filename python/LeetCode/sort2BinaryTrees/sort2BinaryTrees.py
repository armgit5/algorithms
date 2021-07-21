# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/1252968/Java-solution-using-Inorder-traversal

from typing import List, Set, Tuple, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inOrderTraversal(self, root, result):
        if root:
            self.inOrderTraversal(root.left, result)
            result.append(root.val)
            self.inOrderTraversal(root.right, result)
        return result

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result1 = []
        result2 = []
        self.inOrderTraversal(root1, result1)
        self.inOrderTraversal(root2, result2)
        return sorted(result1 + result2)


s = Solution()
one = TreeNode(1)
two = TreeNode(2)
four = TreeNode(4)

one_2 = TreeNode(1)
zero_2 = TreeNode(0)
three_2 = TreeNode(3)

root1 = two
two.left = one
two.right = four

root2 = one_2
one_2.left = zero_2
one_2.right = three_2

print(s.getAllElements(root1, root2))
