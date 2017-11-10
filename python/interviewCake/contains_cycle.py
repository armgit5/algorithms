class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)
d = LinkedListNode(11)

a.next = b
b.next = c
c.next = d
d.next = a


def contains_cycle(first_node):
    fast_runner = first_node
    slow_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next

        if fast_runner is slow_runner:
            return True

    return False

print(contains_cycle(a))
