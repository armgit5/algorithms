package Tree.Inorder;

import java.util.ArrayList;
import java.util.List;


 // Definition for a binary tree node.

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
}


class Solution {

    List<Integer> outputList = new ArrayList<>();

    public List<Integer> inorderTraversal(TreeNode root) {

        if (root == null) return outputList;

        inorderTraversal(root.left);
        outputList.add(root.val);
        inorderTraversal(root.right);

        return outputList;
    }

    public static void main(String[] args) {
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);

        one.right = two;
        two.left = three;

        Solution s = new Solution();
        List<Integer> l = s.inorderTraversal(one);
        System.out.println(l.toString());
    }
}
