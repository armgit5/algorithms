package MyCodeSchool;

public class TimesRotated {

    public static int searchSmallest(int[] array) {
        int low = 0;
        int n =  array.length;
        int high = n - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            // array is sorted
            if (array[low] <= array[high]) {
                return low;
            }

            int next = (mid + 1) % n;
            int prev = (mid + n - 1) % n;

            if (array[mid] <= array[next] && array[mid] > array[prev]) {
                return mid;
            } else if (array[mid] <= array[high])  { // search left side
                high = mid - 1;
            } else {
                low = mid + 1; // search right side
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int A[] = {11,12,15,18,19,2,5,6,8};
        int smallestIndex = searchSmallest(A);
        System.out.println(smallestIndex);
    }
}
