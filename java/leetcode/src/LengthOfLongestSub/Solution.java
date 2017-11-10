package LengthOfLongestSub;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by arm on 7/24/2017 AD.
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
 */
public class Solution {

    public int lengthOfLongestSubstring(String s) {

        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0, j = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)) + 1, i);
            }

            ans = Math.max(ans, j-i+1);
            map.put(s.charAt(j), j);
        }

        System.out.println(ans);
        return ans;
    }

    public int lengthOfLongestSubstringBrute(String s) {

        int maxLength = -1;
        String maxSub = "";

        if (s.length() == 0) {
            return 0;
        }

        for (int i = 0; i < s.length(); i++) {
            String tempS = "";
            for (int j = i; j < s.length(); j++) {
                int hasJ = tempS.indexOf(s.charAt(j));
                if (hasJ < 0) {
                    tempS += s.charAt(j);
                    if (tempS.length() > maxLength) {
                        maxLength = tempS.length();
                        maxSub = tempS;
                    }
                } else {
                    tempS = "" + s.charAt(j);
                }
            }
        }

//        System.out.println(maxSub);
        return maxLength;
    }

    public static void main(String[] args) {
//        String str = "abcabcbb";
//        String str = "bbbbb";
//        String str = "pwwkew";
        String str = "abba";
        Solution sol = new Solution();
//        sol.lengthOfLongestSubstringBrute(str);
        sol.lengthOfLongestSubstring(str);
    }

}
