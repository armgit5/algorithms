package IDeserve.LongestPalindromicSubstring;

public class LongestBrute {
    private static boolean isPalindrome(String s) {
        int n = s.length();
        for (int i = 0; i < (n/2); ++i) {
            if (s.charAt(i) != s.charAt(n - i - 1)) {
                return false;
            }
        }

        return true;
    }

    public static String longestBrute(String s) {
        int max = 0;
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String sub = s.substring(i, j);
                if(isPalindrome(sub) && sub.length() > max) {
                    max = sub.length();
                    longest = sub;
                }
            }
        }
        return longest;
    }

    public static void main(String[] args) {
        // https://www.youtube.com/watch?v=obBdxeCx_Qs
        // Brute force method
        System.out.println(longestBrute("bananas"));

    }
}
