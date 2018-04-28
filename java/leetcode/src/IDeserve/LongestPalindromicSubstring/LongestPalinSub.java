package IDeserve.LongestPalindromicSubstring;

// https://www.youtube.com/watch?v=nbTSfrEfo6M&t=931s
// Need some more work

public class LongestPalinSub {

    public static String longestPalinSubString(String T) {
        int[] P = new int[T.length()];
        int C = 0, R = 0;
        int start = 0, end = 0;
        int max = Integer.MIN_VALUE;

        for (int i = 1; i < T.length()-1; i++) {
            int mirr = 2*C - i;

            if (i < R) {
                P[i] = Math.min(R-i, P[mirr]);
            }

            int atEnd = i+(1+P[i]);
            int atStart = i-(1+P[i]);

            while (T.charAt(atStart) == T.charAt(atEnd)) {
                P[i]++;
                atEnd++;
                atStart--;

                if (atEnd >= T.length() || atStart < 0) {
                    break;
                }

                if (P[i] > max) {
                    max = P[i];
                    end = i+(1+P[i]);
                    start = i-P[i];
                }
            }

            if (i + P[i] > R) {
                C = i;
                R = 1 + P[i];
            }
        }

//        System.out.println(start);
//        System.out.println(end);
        return T.substring(start, end);
//        return "";
    }

    public static String LPS(String s) {
        int n = s.length();
        int palindromeBeginsAt = 0; //index where the longest palindrome begins
        int max_len = 1;//length of the longest palindrome
        boolean palindrome[][] = new boolean[n][n]; //boolean table to store palindrome truth

        //Trivial case: single letter palindromes
        for (int i = 0; i < n; i++) {
            palindrome[i][i] = true;
        }

        //Finding palindromes of two characters.
        for (int i = 0; i < n-1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                palindrome[i][i+1] = true;
                palindromeBeginsAt = i;
                max_len = 2;
            }
        }

        //Finding palindromes of length 3 to n and saving the longest
        for (int curr_len = 3; curr_len <= n; curr_len++) {
            for (int i = 0; i < n-curr_len+1; i++) {
                int j = i+curr_len-1;
                if (s.charAt(i) == s.charAt(j) //1. The first and last characters should match
                        && palindrome[i+1][j-1]) //2. Rest of the substring should be a palindrome
                {
                    palindrome[i][j] = true;
                    palindromeBeginsAt = i;
                    max_len = curr_len;
                }
            }
        }
        return s.substring(palindromeBeginsAt, max_len + palindromeBeginsAt);
    }

    public static void main(String[] args) {
//        String T = "$#A#B#A#B#A#B#A#@";
//        String T = "babad";
        String T = "cbbd";
        System.out.println(longestPalinSubString(T));
        System.out.println(LPS(T));

    }
}
