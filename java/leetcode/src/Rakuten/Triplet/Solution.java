// https://stackoverflow.com/questions/12329711/interview-test-deepest-pit#
// 234 235 578
package Rakuten.Triplet;

import java.util.*;

public class Solution {

    public int solution(int[] A) {
        // write your code in Java SE 8

        int P = -1, Q = -1, R = -1;
        int depth = 0;

        for (int i = 1; i < A.length-1; i++) {

            // set p
            if (Q < 0 && R < 0 && A[i] <= A[i-1] && P < 0) {
                P = i-1;
            }

            // set q
            if (P >= 0 && Q < 0 && A[i] >= A[i-1]) {
                Q = i-1;
            }

            // set r
            // check all possible increasing steps
            if (P >= 0 && Q > 0 && A[i] > A[i-1] || i == A.length-1) {
                R = i;

                System.out.println(P+"  "+Q+"  "+R);
                int tempDept = Math.min(A[P]-A[Q], A[R]-A[Q]);
                depth = Math.max(depth, tempDept);
            }

            // start over
            if (P >= 0 && Q > 0 && A[i] <= A[i-1]) {
                P = i - 1;
                Q = -1;
                R = -1;
            }
        }

        return depth;
    }

    public static void main(String[] args) {
        int[] A = {0,1,3,-2,0,1,0,-3,2,3};
                 //0,1,2, 3,4,5,6, 7,8,9
        Solution s = new Solution();
        int max = s.solution(A);
        System.out.println(max);
    }
}
