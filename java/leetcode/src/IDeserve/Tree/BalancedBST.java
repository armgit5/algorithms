package IDeserve.Tree;
//https://www.youtube.com/watch?v=VCTP81Ij-EM

public class BalancedBST {


    private static TreeNode<Integer> createBST(int[] array, int start, int end) {

        if (start > end) return null;
        int mid = (start + end) / 2;
        TreeNode<Integer> root = new TreeNode(array[mid]);

        root.setLeft(createBST(array, start, mid - 1));
        System.out.print(root.getData());
        root.setRight(createBST(array, mid + 1, end));

        return root;
    }

    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        TreeNode<Integer> root = createBST(arr, 0, arr.length-1);
        System.out.println();
        System.out.println(root.getData());
    }



}
