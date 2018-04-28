// https://www.youtube.com/watch?v=8P-Z7Oc8x9I&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI&index=6

package IDeserve.NextGreater;

import java.util.Stack;

public class NextGreater {

    // Brute force compare
    private static void nextGreaterBrute(Integer[] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = i; j < array.length; j++) {
                if (array[j] > array[i]) {
                    System.out.println("Next greater for " + array[i] + " is " + array[j]);
                    break;
                }
            }
        }
    }

    // O(n) compare using stack
    private static void nextGreater(Integer[] array) {
        Stack<Integer> stack = new Stack<Integer>();
        // Stack is empty, init stack with first element
        stack.push(array[0]);
        for (int i = 1; i < array.length; i++) {
            // While stack is not empty or array[i] > stack.top
            while (!stack.empty() && array[i] > stack.peek())  {
                System.out.println("Next greater element for "
                        + stack.pop() + "\t = " + array[i]);

            }

            stack.push(array[i]);
        }
    }

    public static void main(String[] args) {
        Integer[] array = {98, 23, 54, 12, 55, 7, 27};

        nextGreaterBrute(array);
        nextGreater(array);
    }
}
