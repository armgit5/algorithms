package HackkerRank.Dequeue;

import java.io.File;
import java.io.IOException;
import java.util.*;


public class Solution {

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("leetcode/src/HackkerRank/Dequeue/input.txt"));
//        Scanner in = new Scanner(System.in);
        Deque deque = new ArrayDeque<>();
        HashSet<Integer> set = new HashSet<>();

        int max = 0;

        int n = in.nextInt();
        int m = in.nextInt();

        for (int i = 0; i < n; i++) {
            int num = in.nextInt();

            deque.addLast(num);
            set.add(num);

            if (deque.size() == m) {
                max = set.size() > max ? set.size() : max;
                int first = (int) deque.removeFirst();
                if (!deque.contains(first)) set.remove(first);
            }
        }

        System.out.println(max);
    }
}
