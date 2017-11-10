package IDeserve.BinarySearch;

/**
 * Created by arm on 7/26/2017 AD.
 */
public class FindElementSortedRotatedArray {

    private static int findElementLinear(int[] arr, int num) {

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == num) {
                return i;
            }
        }

        return -1;
    }

    private static int binarySearch(int[] arr, int num, int start, int end) {

        if(start > end || start < 0 || end >= arr.length) {
            throw new IllegalArgumentException("Invalid values for start and end! start = " + start + ", end = " + end);
        }

        if(num < arr[start] || num > arr[end]) {
            return -1;
        }

        while (start <= end) {
            int mid = (start + end) / 2;
            if (num == arr[mid]) {
                return mid;
            }
            if (num > mid) {
                start = mid + 1;
            } else {
                end = mid -1;
            }
        }

        return -1;
    }

    private static int findElementWithoutPivot(int[] arr, int num) {
        if (arr.length == 0 || arr == null) {
            return -1;
        }

        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (arr[mid] == num) {
                return mid;
            }

            // left is sorted
            if (arr[mid] >= arr[start]) {
                if (arr[start] <= num && num < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (arr[mid] < num && num <= arr[end]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }

        return -1;
    }

    private static int findElement(int[] arr, int num) {

        if (arr.length == 0 || arr == null) {
            return -1;
        }

        int pivot = FindAPivot.findPivotBinary(arr);

        if (num == arr[pivot]) {
            return pivot;
        } else if (num > arr[pivot]) {
            return binarySearch(arr, num, pivot, arr.length - 1);
        } else {
            return binarySearch(arr, num, 0, pivot - 1);
        }

    }

    public static void main(String[] args) {
        int[] array = {73, 85, 94, 21, 27, 34, 47, 54, 66};
//        System.out.println(FindAPivot.findPivotBinary(array));
//        System.out.println(findElementLinear(array, 34));
        System.out.println(findElementWithoutPivot(array, 34));
    }


}
