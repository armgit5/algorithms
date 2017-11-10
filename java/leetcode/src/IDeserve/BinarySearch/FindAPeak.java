package IDeserve.BinarySearch;

/**
 * Created by arm on 7/27/2017 AD.
 */
public class FindAPeak {

    private static int findPeak(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if ((mid == 0 || arr[mid - 1] <= arr[mid]) && (mid == arr.length - 1 || arr[mid] >= arr[mid + 1])) {
                return mid;
            }

            // left is greater
            if (mid > 0 && arr[mid - 1] > arr[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }

        }

        return -1;
    }


    public static void main(String[] args) {
//        int[] array = {73, 85, 94, 21, 27, 34, 47, 54, 66};
//        int[] array = {5, 5, 5, 0, 1, 2, 5};

        int[] array = {5, 10, 15, 25, 30, 45, 50, 65, 35, 1};
//        int[] array = {1,4,3,6,7,5};
        int peakPoint = findPeak(array);
        System.out.println(peakPoint);
//        System.out.println(array[peakPoint]);
    }

}
