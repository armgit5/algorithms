# https://www.youtube.com/watch?v=SmnUqWmWvz0&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=39
# 1 - - -> 2
# ^        |
# | -> 3   |
# |        v
# 4 < - -  5

# shortestPath(2,3) = 2 -> 5 -> 4 -> 3
# using breath first search to search for shortest path


class Node():
    def __init__(self, value):
        self.value = value
        self.next = []

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next.append(two)
two.next.append(five)
five.next.append(four)
four.next.append(one)
four.next.append(three)

def shortestPath(a, b):

    # Check if a or b is null
    if a == None or b == None: return None

    # Make a queue for breatch first search
    # starting from a node
    toVisit = [a]

    # Parent hash map is make sure the path
    # is not going back to parent node
    parents = {a.value: None}

    # Traverse from the beginning to the end
    while len(toVisit) != 0:
        # Pop the first node
        curr = toVisit.pop(0)

        # If it's b then break
        if curr == b: break

        # Check for neighbor nodes
        for n in curr.next:
            # Check if we have already travel to n node before
            # n should not be in parents hash map
            # then add to the queue to travel next
            if n.value not in parents:
                toVisit.append(n)
                parents[n.value] = curr.value

    # If no b in parents then no path to b
    if b.value not in parents: return None

    out = [] # out list
    curr_val = b.value
    while curr_val != None:
        out.insert(0, curr_val)
        curr_val = parents[curr_val]

    print(out)

shortestPath(two, three)
