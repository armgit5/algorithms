// https://www.youtube.com/watch?v=hmWhJyz5kqc&index=9&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI

package IDeserve.Tree;

public class MinBinTree {

    // Find min depth of a binary tree
    private static Integer getMinDepthBinTree(TreeNode root) {

        if (root == null) {
            return 0;
        }

        // Is a leaf node
        if (root.getLeft() == null && root.getRight() == null) {
            return 1;
        }

        int leftDepth = root.getLeft() != null ? getMinDepthBinTree(root.getLeft()) : Integer.MAX_VALUE;
        int rightDepth = root.getRight() != null ? getMinDepthBinTree(root.getRight()) : Integer.MAX_VALUE;

        return 1 + Math.min(leftDepth, rightDepth);
    }

    public static void main(String[] args) {
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);
        TreeNode four = new TreeNode(4);
        TreeNode five = new TreeNode(5);
        TreeNode six = new TreeNode(6);

        one.setLeft(two);
        one.setRight(three);
        three.setLeft(four);
        three.setRight(five);
        four.setLeft(six);

        int minDepth = getMinDepthBinTree(one);
        System.out.println(minDepth);
    }

}
