// https://www.youtube.com/watch?v=fCGLjlsEsNA&index=9&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI
// Array look up time is O(n)
// Time com = O(n) and space = O(1)

package IDeserve.MaxAvgSub;

public class MaxAvgSub {

    public static Integer maxAvgSub(int[] arr, int k) {

        int n = arr.length;
        // Test case
        if (k > n || k == n) {
            return 0;
        }

        // Initialize first sum
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += arr[i];
        }

        // Find max sum from remaining sub array
        int maxSum = sum;
        for (int i = k; i < n; i++) {
            sum = sum + arr[i] - arr[i - k];
            if (maxSum < sum) {
                maxSum = sum;
            }
        }

        return maxSum;

    }

    public static void main(String[] args) {
        int[] input = {11, -8, 16, -7, 24, -2, 3};
        int k = 3;

        System.out.println(maxAvgSub(input, k));
    }
}
