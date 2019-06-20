// https://leetcode.com/problems/longest-mountain-in-array/description/
//
//Input: [2,1,4,7,3,2,5]
//Output: 5
//Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
//
//Input: [2,2,2]
//Output: 0
//Explanation: There is no mountain.

package LogestMountainArray;

public class LongestMountainArray {

    private static int longestMountain(int[] A) {
        int N = A.length;
        int base = 0, ans = 0;

        // Loop from start to end
        while (base < N) {
            int end = base;

            // base is the start of the mountian so that it goes up first
            // before coming down
            if (end + 1 < N && A[end] < A[end+1]) {
                // Walk to the top of the mountain
                while (end + 1 < N && A[end] < A[end+1]) end++;

                // before taking end into account check to see if it's coming down
                // if it's not coming down, end will not be affecting ans
                if (end + 1 < N && A[end] > A[end+1]) {
                    // If already on the top of the mountain
                    while (end + 1 < N && A[end] > A[end+1]) end++;

                    ans = Math.max(ans, end - base + 1);
                }
            }

            base = Math.max(end, base + 1);
        }


        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {2, 1, 4, 7, 3, 2, 5};
        int[] arr2 = {2, 2, 2};
        int[] arr3 = {2, 3, 2, 3, 4, 5, 6, 7};
        int ans = longestMountain(arr);
        int ans2 = longestMountain(arr2);
        int ans3 = longestMountain(arr3);

        System.out.println(ans);
        System.out.println(ans2);
        System.out.println(ans3);
    }
}
