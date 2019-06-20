// https://www.youtube.com/watch?v=nll-b4GeiX4&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=24


package ByteByByte.SortStacks;

import java.util.Stack;

public class SortStacks {

    private static Stack<Integer> sortStack(Stack<Integer> stack) {
        // Return stack if stack is null or empty
        if (stack == null || stack.isEmpty()) return stack;

        // Create new stack to sort
        Stack<Integer> newStack = new Stack<Integer>();
        newStack.push(stack.pop());

        // Loop original stack to move all elements to new stack
        while (!stack.isEmpty()) {

            int temp = stack.pop(); // temp var

            // Check new stack if new element coming in is greater than the
            // last element in new stack
            while (!newStack.isEmpty() && temp > newStack.peek()) {
                stack.push(newStack.pop());
            }

            // push temp var as largest to new stack's bottom
            newStack.push(temp);
        }

        return newStack;
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(1);
        stack.push(3);
        stack.push(2);
        stack.push(4);

        Stack<Integer> sortedStack = sortStack(stack);
        System.out.println(sortedStack.toString());
    }
}
