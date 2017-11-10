package IDeserve.Tree;


public class LowestCommonAncestor {

    public static TreeNode getLCA(TreeNode curr, TreeNode A, TreeNode B) {

        if (curr == null) {
            return null;
        }

        if (curr == A || curr == B) {
            return curr;
        }

        TreeNode left = getLCA(curr.getLeft(), A, B);
        TreeNode right = getLCA(curr.getRight(), A, B);

        if (left != null && right != null) {
            return curr;
        }

        if (left == null) return right; else return left;
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5, new TreeNode(7), new TreeNode(8))), new TreeNode(3));
        TreeNode A = root.getLeft().getLeft();   // Node 4
        TreeNode B = root.getLeft().getRight().getRight();            // Node 8
        TreeNode lca = getLCA(root, A, B);
        System.out.println(lca.getData());
    }
}
