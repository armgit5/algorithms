# https://leetcode.com/problems/binary-tree-preorder-traversal/
# recursion https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# wihtout recursion https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/1258233/an-easy-and-unified-way-of-doing-preorder-and-postorder-iteratively


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                self.arr.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)

        return self.arr

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root == None:
    #         return root
    #     self.arr.append(root.val)
    #     self.preorderTraversal(root.left)
    #     self.preorderTraversal(root.right)
    #
    #     return self.arr

s = Solution()

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

one.right = two
two.left = three

print(s.preorderTraversal(one))

l = [1,2,3]
l.extend([6,None,7])
print(l)

