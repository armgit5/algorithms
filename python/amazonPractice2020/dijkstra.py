# https://www.youtube.com/watch?v=cbow7Y2uDq8


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None
        self.visited = []
        self.parent_dist = 0


root = Node(0)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

