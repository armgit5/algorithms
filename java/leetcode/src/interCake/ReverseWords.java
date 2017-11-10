package interCake;

/**
 * Created by arm on 8/4/2017 AD.
 */
public class ReverseWords {

    public static String reverseWords(String message) {
        char[] chars = message.toCharArray();

        reverseCharacters(chars, 0, message.length()-1);

        int startIndex = 0;
        for (int i = 0; i <= chars.length; i++) {

            if (i == chars.length || chars[i] == ' ') {
                reverseCharacters(chars, startIndex, i - 1);
                startIndex = i + 1;
            }


        }

        return new String(chars);
    }

    public static String reverseCharacters(char[] chars, int start, int end) {

        while (start < end) {
            char temp =  chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start++;
            end--;
        }

        return new String(chars);
    }

    public static void main(String[] args) {
//        String message = "find you will pain only go you recordings security the into if";
        String message = "the eagle has landed";
        String rev = reverseWords(message);
        System.out.println(rev);

//        char[] chars = message.toCharArray();
//        String a = reverseCharacters(chars, 0, message.length() - 1);
//        System.out.println(a);
    }

}
