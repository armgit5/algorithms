package interCake.BalanceBinaryTree;

//https://www.interviewcake.com/question/java/balanced-binary-tree?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email
//https://www.youtube.com/watch?v=TWDigbwxuB4

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class NodeDepthPair {

    BinaryTreeNode node;
    int depth;

    NodeDepthPair(BinaryTreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}

public class BinaryTreeNode {
    public int value;
    public BinaryTreeNode left;
    public BinaryTreeNode right;

    public BinaryTreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public BinaryTreeNode insertLeft(int leftValue) {
        this.left = new BinaryTreeNode(leftValue);
        return this.left;
    }

    public BinaryTreeNode insertRight(int rightValue) {
        this.right = new BinaryTreeNode(rightValue);
        return this.right;
    }

    static boolean isSuperBalanced(BinaryTreeNode treeRoot) {

        if (treeRoot == null) {
            return true;
        }

        List<Integer> depths = new ArrayList<>(3);
        Stack<NodeDepthPair> nodes = new Stack<>();
        nodes.push(new NodeDepthPair(treeRoot, 0));

        while (!nodes.empty()) {
            NodeDepthPair nodeDepthPair = nodes.pop();
            BinaryTreeNode node = nodeDepthPair.node;
            int depth = nodeDepthPair.depth;

            if (node.left == null && node.right == null) {

                if (!depths.contains(depth)) {
                    depths.add(depth);

                    if (depths.size() > 2 || (depths.size() == 2 &&
                        Math.abs(depths.get(0) - depths.get(1)) > 1)) {
                        return false;
                    }
                }

            } else {
                if (node.right != null) {
                    nodes.push(new NodeDepthPair(node.right, depth + 1));
                }
                if (node.left != null) {
                    nodes.push(new NodeDepthPair(node.left, depth + 1));
                }
            }
        }


        return true;
    }

    static boolean isBalancedRecursive(BinaryTreeNode n) {
        if (n == null) {
            return true;
        }

        if (isBalancedRecursiveHelper(n) > -1) {
            return true;
        } else {
            return false;
        }
    }

    static int isBalancedRecursiveHelper(BinaryTreeNode n) {
        if (n == null) {
            return 0;
        }

        int leftHeight = isBalancedRecursiveHelper(n.left);
        if (leftHeight == -1) {
            return -1;
        }

        int rightHeight = isBalancedRecursiveHelper(n.right);
        if (rightHeight == -1) {
            return -1;
        }

        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }

        return 1 + Math.max(leftHeight, rightHeight);

    }

 /*
                            3
                      1             5
                  0      2       4
                                   6
    */

    public static void main(String[] args) {
        BinaryTreeNode zero = new BinaryTreeNode(0);
        BinaryTreeNode one = new BinaryTreeNode(1);
        BinaryTreeNode two = new BinaryTreeNode(2);
        BinaryTreeNode three = new BinaryTreeNode(3);
        BinaryTreeNode four = new BinaryTreeNode(4);
        BinaryTreeNode five = new BinaryTreeNode(5);
        BinaryTreeNode six = new BinaryTreeNode(6);

        three.left = one;
        one.left = zero;
        one.right = two;
        three.right = five;
        five.left = four;
        four.right = six;

        System.out.println(isSuperBalanced(three));

        if (isBalancedRecursive(three)) {
            System.out.print("max level = ");
            System.out.print(isBalancedRecursiveHelper(three) - 1);
        } else {
            System.out.println("not balanced");
        }

        System.out.println(isBalancedRecursive(zero));

    }
}
