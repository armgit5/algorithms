package IDeserve.LinkedList;

// https://www.youtube.com/watch?v=apIw0Opq5nk&index=5&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI

public class DetectLoop {

    private static MyLinkedList.node startOfALoop(MyLinkedList list) {
        MyLinkedList.node S = list.head, F = list.head;

        while (S.next != null && F.next != null) {
            S = S.next;
            F = F.next.next;

            if (S == F) {
                S = list.head;
                break;
            }
        }

        while (S.next != null && F.next != null) {
            S = S.next;
            F = F.next;

            if (S == F) {
                return S;
            }

        }

        return null;
    }

    private static boolean isALoop(MyLinkedList list) {
        MyLinkedList.node S = list.head, F = list.head;

        while (S.next != null && F.next != null) {
            S = S.next;
            F = F.next.next;

            if (S == F) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {

        MyLinkedList list = new MyLinkedList();

        list.addNode_Tail(8);
        list.addNode_Tail(1);
        list.addNode_Tail(9);
        list.addNode_Tail(4);
        MyLinkedList.node two = list.addNode_Tail(2);

        list.addNode_Tail(3);
        list.addNode_Tail(7);
        list.addNode_Tail(2);
        MyLinkedList.node nine = list.addNode_Tail(9);
        nine.next = two;

        System.out.println(isALoop(list));

        MyLinkedList.node start = startOfALoop(list);
        if (start != null) {
            System.out.println(start.data);
        }

    }
}
