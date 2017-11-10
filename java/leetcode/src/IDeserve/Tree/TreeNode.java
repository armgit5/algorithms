package IDeserve.Tree;

public class TreeNode<T> {

    private T data;
    private TreeNode left;
    private TreeNode right;

    public TreeNode(T data, TreeNode left, TreeNode right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    public TreeNode(T data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public TreeNode getLeft() {
        return left;
    }

    public void setLeft(TreeNode left) {
        this.left = left;
    }

    public TreeNode getRight() {
        return right;
    }

    public void setRight(TreeNode right) {
        this.right = right;
    }

//    public void insert(TreeNode root, T data) {
//        if (root == null) {
//            root = new TreeNode(data);
//        }
//
//
//        if (data. < 0) {
//
//        }
//    }

}
