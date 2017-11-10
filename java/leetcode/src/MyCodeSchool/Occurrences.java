package MyCodeSchool;

public class Occurrences {

    private static int BinarySearch(int[] array, int n, int x, boolean searchFirst) {

        int low = 0, high = n - 1, result = -1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (array[mid] == x) {
                result = mid;
                if (searchFirst) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (x > array[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int A[] = {1,1,3,3,5,5,5,5,5,9,9,11};
        int x = 9;
        int firstIndex = BinarySearch(A, A.length, x, true);

        if (firstIndex == -1) {
            System.out.println("Count is 0");
        } else {
            int lastIndex = BinarySearch(A, A.length, x, false);
            System.out.println(firstIndex + " " + lastIndex);
            System.out.println("Count is " + (lastIndex - firstIndex + 1));
        }
    }
}
