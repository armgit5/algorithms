//https://leetcode.com/problems/longest-repeating-character-replacement/discuss/


package String.LongestRepeating;

public class Solution {

    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < s.length(); end++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            while (end - start + 1 - maxCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        String s = "AABABBA";
        int k = 1;
//        String s = "ABAB";
//        int k = 2;

        Solution so = new Solution();
        int maxLength = so.characterReplacement(s, k);
        System.out.println(maxLength);
    }
}


