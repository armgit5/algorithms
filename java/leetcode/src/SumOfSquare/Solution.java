package SumOfSquare;

public class Solution {

    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int num = 2147483646;
        Solution s = new Solution();
        System.out.println(s.judgeSquareSum(num));

    }
}
