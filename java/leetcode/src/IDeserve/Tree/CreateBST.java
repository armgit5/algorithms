//https://www.youtube.com/watch?v=VCTP81Ij-EM&index=2&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI

package IDeserve.Tree;

public class CreateBST {

    public static TreeNode createBST(int[] array, int start, int end) {

        if (start > end) return null;
        int mid = (start + end) / 2;
        TreeNode root = new TreeNode(array[mid]);
        root.setLeft(createBST(array, start, mid - 1));
        root.setRight(createBST(array, mid + 1, end));

        return root;
    }

    public static void main(String[] args) {
        int[] array = {1,2,3,4,5,6,7,8,9};
        TreeNode root = createBST(array, 0, array.length - 1);
        System.out.println(root.getData());
    }
}
