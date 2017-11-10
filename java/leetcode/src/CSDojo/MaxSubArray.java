package CSDojo;
// https://www.youtube.com/watch?v=pnzZzbQ3ZAY&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=8
// https://www.youtube.com/watch?v=ohHWQf1HDfU


import java.util.Arrays;

public class MaxSubArray {

    public static int maxSub(int[] a, int n) {
        int ans = 0, sum = 0, max = -Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            sum += a[i];
            if (sum < 0) {
                sum = 0;
            }
            ans = Math.max(sum, ans);

            max = Math.max(a[i], max);
        }

        if (ans == 0) {
            return max;
        }
        return ans;
    }

    public static int maxSubDivide(int[] a, int n) {
        if (n == 1) {
            return a[0];
        }

        int m = n / 2;
        int leff_MSS = maxSubDivide(Arrays.copyOfRange(a, 0, m), m);
        int right_MSS = maxSubDivide(Arrays.copyOfRange(a, m, n), n-m);
        int leftsum = Integer.MIN_VALUE, rightsum = Integer.MIN_VALUE, sum = 0;
        for (int i = m; i < n; i++) {
            sum += a[i];
            rightsum = Math.max(sum, rightsum);
        }
        sum = 0;
        for (int i = m-1; i >= 0; i--) {
            sum += a[i];
            leftsum = Math.max(sum, leftsum);
        }
        int ans = Math.max(leftsum, rightsum);
        return Math.max(ans, leftsum + rightsum);

    }

    public static int maxSubBruteO2(int[] a, int n) {
        int ans = Integer.MIN_VALUE;
        for (int startIndex = 0; startIndex < n; startIndex++) {
            int sum = 0;
            for (int subArraySize = 1; subArraySize <= n; subArraySize++) {
                if (startIndex + subArraySize > n) break;
                sum += a[startIndex + subArraySize - 1];
                ans = Math.max(ans, sum);
            }

        }
        return ans;
    }

    public static int maxSubBruteO3(int[] a, int n) {
        int ans = Integer.MIN_VALUE;
        for (int subArraySize = 1; subArraySize <= n; subArraySize++) {
            for (int startIndex = 0; startIndex < n; startIndex++) {
                if (startIndex + subArraySize > n) {
                    break;
                }
                int sum = 0;
                for (int i = startIndex; i < (startIndex + subArraySize); i++) {
                    sum += a[i];
                }
                ans = Math.max(ans, sum);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] a1 = {1,-3,2,1,-1};
        int[] a2 = {-2,1,-3,4,-1,2,1,-5,4};
        int[] a3 = {-1,-2,-5};

//        System.out.println(maxSubBruteO3(a2, a2.length));
//        System.out.println(maxSubBruteO2(a2, a2.length));
//        System.out.println(maxSubDivide(a2, a2.length));
//        System.out.println(maxSub(a2, a2.length));
        System.out.println(maxSub(a3, a3.length));
    }
}
