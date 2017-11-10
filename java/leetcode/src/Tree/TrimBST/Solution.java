package Tree.TrimBST;

// Definition for a binary tree node.
//https://leetcode.com/problems/trim-a-binary-search-tree/description/

import IDeserve.Tree.Inorder;

import java.util.ArrayList;
import java.util.List;

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
//        outputList.add(root.val);
        System.out.println(root.val);
        inorderTraversal(root.right);

        return outputList;
    }


    public TreeNode trimBST(TreeNode root, int L, int R) {
        if (root == null) return null;

        if (root.val < L) return trimBST(root.right, L, R);
        if (root.val > R) return trimBST(root.left, L, R);

        root.left = trimBST(root.left, L, R);
        root.right = trimBST(root.right, L, R);

        return root;
    }

    public static void main(String[] args) {
        TreeNode zero = new TreeNode(0);
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);
        TreeNode four = new TreeNode(4);

//        one.left = zero;
//        one.right = two;
//
//        Solution s = new Solution();
//        s.trimBST(one, 1, 2);
//        s.inorderTraversal(one);

        three.left = zero;
        zero.right = two;
        two.left = one;
        three.right = four;

        Solution s = new Solution();
        s.trimBST(three, 1, 3);
        s.inorderTraversal(three);

    }
}
