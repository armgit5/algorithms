package IDeserve.LinkedList;

public class MyLinkedList {

    class node
    {
        int data;
        node next;

        node(int data)
        {
            this.data = data;
        }
    }

    node head;
    node tail;

    MyLinkedList() {
    }

    MyLinkedList(int data) {
        node n1 = new node(data);
        this.head = n1;
        this.tail = n1;
    }

    public node addNode_Tail(int data) {
        // if we have an empty list, create a new list and copy its head and tail into
        // current object
        if (this.head == null)
        {
            MyLinkedList l_temp = (new MyLinkedList(data));
            this.head = l_temp.head;
            this.tail = l_temp.tail;
            return null;
        }

        // we need to add this node 'n' to the end of the list
        node n = new node(data);

        node current = this.head, prev = null;

        while (current != null)
        {
            prev = current;
            current = current.next;
        }

        prev.next = n;
        this.tail = n; // update the tail info as well

        return n;
    }



}
