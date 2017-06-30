class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if counter < 1:
            return None
        while counter <= position and current:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        counter = 1
        if position > 1:
            while counter < position and current:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        if position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while value != self.head.value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def reverse(self):
        current = self.head
        prev = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_recur(self, node):

        if node.next == None:
            self.head = node
            return

        self.reverse_recur(node.next)
        temp = node.next
        temp.next = node
        node.next = None

    def reverse_stack(self):
        stack = []
        current = self.head
        while current != None:
            stack.append(current)
            current = current.next

        temp = stack.pop()
        self.head = temp
        while len(stack) != 0:
            a = temp.value
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None


    def to_string(self):
        current = self.head

        while current.next:
            print((current.value))
            current = current.next
        print((current.value))

    def to_string_recur(self, head):

        if head == None:
            return

        print((head.value))
        self.to_string_recur(head.next)

    def to_string_recur_rev(self, head):

        if head == None:
            return
        self.to_string_recur_rev(head.next)
        print((head.value))



def reverseStack(s):
    stack = []
    text = ""
    for i in s:
        stack.append(i)

    for i in range(len(s)):
        text += stack.pop()

    return text

# s = "hello"
# print reverseStack(s)

# Test cases
# Set up some Elements
e1 = Element(2)
e2 = Element(4)
e3 = Element(6)
e4 = Element(8)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)


# ll.to_string()
# ll.reverse()
# ll.to_string()
# ll.to_string_recur(e2)
# ll.to_string_recur_rev(e2)

# ll.to_string()
# ll.reverse_recur(e1)
# ll.to_string()

ll.reverse_stack()
ll.to_string()