package AddTwoNumber;

import java.lang.reflect.Array;
import java.util.List;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {

    public static class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
    }

    private void printListNode(ListNode resultN) {
        System.out.println(resultN.val);
        while (resultN.next != null) {
            System.out.println(resultN.next.val);
            resultN = resultN.next;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode current = new ListNode(0), head = current;
        ListNode p = l1, q = l2;
        int carry = 0;

        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }

        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        return head.next;
    }

    public ListNode addTwoNumbersSimple(ListNode l1, ListNode l2) {
        int var1 = l1.val;
        int var2 = l2.val;
        int count = 1;

        ListNode templ1 = l1;
        ListNode templ2 = l2;
        ListNode resultN = null;


        while (templ1.next != null) {
            var1 = (int) (var1 + templ1.next.val * Math.pow(10, count));
            count++;
            templ1 = templ1.next;
        }

        count = 1;
        while (templ2.next != null) {
            var2 = (int) (var2 + templ2.next.val * Math.pow(10, count));
            count++;
            templ2 = templ2.next;
        }

        int sum = var1 + var2;
        ListNode head = new ListNode(0);
        while (sum != 0) {
            if (resultN == null) {
                resultN = new ListNode(sum % 10);
                head = resultN;
            } else {
                while (resultN.next != null) {
                    resultN = resultN.next;
                }
                resultN.next = new ListNode(sum % 10);
            }
            sum /= 10;
        }

        return head;
    }

    public static void main(String[] args) {

//        int[] list1 = {9};
//        int[] list2 = {1,9,9,9,9,9,9,9,9,9};

//        int[] list1 = {2, 4, 3};
//        int[] list2 = {5, 6, 4};

        int[] list1 = {5};
        int[] list2 = {5};

//        int[] list1 = {0};
//        int[] list2 = {0};

        ListNode ln1 = null;
        ListNode ln2 = null;
        ListNode temp = null;

        for (int i: list1) {
            if (temp == null) {
                temp = new ListNode(i);
                ln1 =  temp;
            } else {
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = new ListNode(i);
            }
        }

        temp = null;
        for (int i: list2) {
            if (temp == null) {
                temp = new ListNode(i);
                ln2 =  temp;
            } else {
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = new ListNode(i);
            }
        }

        Solution s = new Solution();
        ListNode resultN = s.addTwoNumbers(ln1, ln2);
        s.printListNode(resultN);
    }

}