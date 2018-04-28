// https://www.youtube.com/watch?v=obBdxeCx_Qs

package IDeserve.LongestPalindromicSubstring;

public class LongestDynamic {

    private static String longestDynamic(String s) {
        int n = s.length();
        int parlindromeBeginAt = 0;
        int maxLength = 0;
        boolean palindrome[][] = new boolean[n][n];
        
        // Single letter trivial
        for (int i = 0; i < n; i++) {
            palindrome[i][i] = true;
        }

        // 2 Characters trivial
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                parlindromeBeginAt = i;
                palindrome[i][i+1] = true;
                maxLength = 2;
            }
        }

        // 3 Or more charecters
        for (int currLength = 3; currLength < n; currLength++) {
            for (int i = 0; i <= n - currLength; i++) {
                int j = i + currLength - 1;

                // First and last chars should match
                // and rest of substring should be palindrome
                if (s.charAt(i) == s.charAt(j) && palindrome[i+1][j-1]) {
                    palindrome[i][j] = true;
                    parlindromeBeginAt = i;
                    maxLength = currLength;
                }
            }
        }

        return s.substring(parlindromeBeginAt, maxLength + 1);


    }

    public static void main(String[] args) {
        String s = "bananas";
        System.out.println(longestDynamic(s));
    }
}
