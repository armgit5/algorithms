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

    def to_string(self):
        current = self.head

        while current.next:
            print current.value
            current = current.next
        print current.value




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

