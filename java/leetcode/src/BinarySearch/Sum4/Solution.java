package BinarySearch.Sum4;

import java.util.HashMap;

/**
 * Created by arm on 7/29/2017 AD.
 */
public class Solution {

    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;

        // compute a + b
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                int sum = A[i] + B[j];

                if (map.containsKey(sum)) {
                    map.put(sum, map.get(sum) + 1);
                } else {
                    map.put(sum, 1);
                }
            }
        }

        // compute c + d
        for (int i = 0; i < C.length; i++) {
            for (int j = 0; j < D.length; j++) {
                int sum = -(C[i] + D[j]);

                if (map.containsKey(sum)) {
                    count += map.get(sum);
                }
            }
        }

        return count;

    }

    public static void main(String[] args) {
        int[] A = {1, 2};
        int[] B = {-2, -1};
        int[] C = {-1, 2};
        int[] D = {0, 2};

        Solution s = new Solution();
        System.out.println(s.fourSumCount(A, B, C, D));

    }
}
