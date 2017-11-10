package IDeserve.BinarySearch;

/**
 * Created by arm on 7/29/2017 AD.
 * https://www.youtube.com/watch?v=MHNTl_NvOj0&index=6&list=PLamzFoFxwoNhR2uFoqm6nr8VgsERgTmYy
 */
public class MedianOfTwoSorted {

    public static double findMedianSortedArrays(int[] a, int[] b, int startA, int endA, int startB, int endB) {

        // case 1
        if ((endA - startA == 1) && (endB - startB == 1)) {
            return (1.0 * (Math.max(a[startA], b[startB]) + Math.min(a[endA], b[endB])) / 2);
        }

        int m1Index = (startA + endA) / 2;
        int m2Index = (startB + endB) / 2;

        int m1 = a[m1Index];
        int m2 = b[m2Index];

        // case 2
        if (m2 == m1) {
            return m2;
        }

        // case 3
        if (m1 < m2) {
            startA = m1Index;
            endB = m2Index;
        } else {
            startB = m2Index;
            endA = m1Index;
        }

        return findMedianSortedArrays(a, b, startA, endA, startB, endB);
    }


    public static void main(String[] args) {
//        int[] arrA = {1, 2, 5, 11, 15};
//        int[] arrB = {3, 4, 13, 17, 18};

        int[] arrA = {1, 3, 5, 11, 15};
        int[] arrB = {9, 10, 11, 13, 14};

        int n = arrA.length - 1;
        System.out.println(findMedianSortedArrays(arrA, arrB, 0, n, 0, n));
    }

}
