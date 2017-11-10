package IDeserve.BinarySearch;

/**
 * Created by arm on 7/24/2017 AD.
 */
public class FindAPivot {

    private static int findPivotLinear(int[] array) {

        if (array.length == 0 || array == null) {
            return -1;
        }

        for (int i = 0; i < array.length - 1; i++) {
            if (array[i + 1] < array[i]) {
                return i + 1;
            }
        }
        return 0;
    }

    static int findPivotBinary(int[] array) {

        if (array.length == 0 || array == null) {
            return -1;
        }

        if (array[0] < array[array.length - 1] || array.length == 1) {
            return 0;
        }

        int start = 0;
        int end = array.length - 1;


        while (start <= end) {
            int mid = (start + end) / 2;

            if (array[mid + 1] < array[mid]) {
                return mid + 1;
            }

            if (array[start] <= array[mid]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return -1;


    }

    public static void main(String[] args) {
//        int[] array = {73, 85, 94, 21, 27, 34, 47, 54, 66};
        int[] array = {5, 5, 5, 0, 1, 2, 5};
        int pivot = findPivotLinear(array);
        int pivotBinary = findPivotBinary(array);
        System.out.println(pivot);
        System.out.println(pivotBinary);
    }
}
