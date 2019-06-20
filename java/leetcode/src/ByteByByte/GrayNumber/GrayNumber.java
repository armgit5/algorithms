package ByteByByte.GrayNumber;
// if 2 integrers are different by a single bit, will not be gray number
//       1 and 2
//      01    10
// xor   1     1 = false
// https://www.youtube.com/watch?v=LqxtPV8xKeI&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=20

public class GrayNumber {

    private static boolean isGrayV1(int a, int b) {
        int x = a ^ b;
        int count = 0;
        while (x > 0) {
            // Check last digit for 1 and digit to the left is 1
            if (x % 2 == 1) {
                count += 1;
            }
            x = x >> 1;
        }
        return count < 2;
    }

    private static boolean isGrayV2(int a, int b) {
        int x = a ^ b;
        return (x & (x - 1)) == 0;
    }

    public static void main(String[] args) {
        System.out.println(isGrayV1(0, 1));
        System.out.println(isGrayV1(1, 2));

        System.out.println(isGrayV2(0, 1));
        System.out.println(isGrayV2(1, 2));
    }
}
