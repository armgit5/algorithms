// https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
//Input :
//        arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
//        k = 3
//        Output :
//        3 3 4 5 5 5 6


package GeeksForGeeks;

import java.util.Deque;
import java.util.LinkedList;

public class SlidingWindowMax {

    private static void maxArrSimple(int[] arr, int k) {

        int N = arr.length;

        // Loop first ele to last - k
        for (int i = 0; i <= N - k; i++) {
            int max = arr[i];
            // Find max in k window
            for (int j = 0; j < k; j++) {
                // Set max for each window
                if (arr[i + j] > max) {
                    max = arr[i + j];
                }
            }
            // Print out max ele in each windows
            System.out.print(max +  " ");
        }
    }

    private static void maxArr(int[] arr, int k) {

        int N = arr.length;
        Deque<Integer> Q = new LinkedList<Integer>();

        // First max in window
        // Add max in the Q from arr[0] to arr[i]
        for (int i = 0; i < k; i++) {

            // Remove small elements from Q to find max
            // Max will be in the front of the Q
            while(!Q.isEmpty() && arr[i] >= arr[Q.peekLast()])
                Q.removeLast();

            Q.addLast(i);
        }

        // Find max from arr[k] to arr[n-1]
        for (int i = k; i < N; i++) {

            // Print max
            Integer max = arr[Q.peek()];
            System.out.print(max + " ");

            // Remove the elements which are out of this window
            while((!Q.isEmpty()) && Q.peek() <= i-k)
                Q.removeFirst();

            // Start over again
            // Remove small elements from Q to find max
            // Max will be in the front of the Q
            while((!Q.isEmpty()) && arr[i] >= arr[Q.peekLast()])
                Q.removeLast();

            // Add curernt max to Q
            Q.addLast(i);

        }

        // Print max
        Integer max = arr[Q.peekFirst()];
        System.out.print(max + " ");

    }


    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 1, 4, 5, 2, 3, 6};

        maxArrSimple(arr, 3);
        System.out.println();
        maxArr(arr, 3);
    }
}


