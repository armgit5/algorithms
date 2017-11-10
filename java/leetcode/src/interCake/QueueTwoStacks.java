//https://www.interviewcake.com/question/java/queue-two-stacks?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email

package interCake;

import java.util.Stack;

public class QueueTwoStacks {

    Stack<String> inStack = new Stack<>();
    Stack<String> outStack = new Stack<>();

    public void enqueue(String item) {
        inStack.add(item);
    }

    public String dequeue() {

        if (outStack.empty()) {

            while (!inStack.empty()) {
                outStack.push(inStack.pop());
            }
        }

        return outStack.pop();
    }

    public Stack<String> getInStack() {
        return inStack;
    }

    public Stack<String> getOutStack() {
        return outStack;
    }

    public static void main(String[] args) {

        QueueTwoStacks q = new QueueTwoStacks();
        q.enqueue("A");
        q.enqueue("B");
        q.enqueue("C");
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        q.enqueue("D");
        System.out.println(q.dequeue());
        q.enqueue("E");
        System.out.println(q.dequeue());
        System.out.println(q.getInStack().empty());
        System.out.println(q.getOutStack().empty());

    }
}
